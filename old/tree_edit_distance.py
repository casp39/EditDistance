import collections
import numpy as np

from tree import Node, AnnotatedTree

def strdist(a, b):
    if a == b:
        return 0
    else:
        return 1

class Operation(object):
    remove = 0
    insert = 1
    update = 2
    match = 3

    def __init__(self, op, arg1=None, arg2=None):
        self.type = op
        self.arg1 = arg1
        self.arg2 = arg2

    def __repr__(self):
        if self.type == self.remove:
            return '<Operation Remove: ' + self.arg1.label + '>'
        elif self.type == self.insert:
            return '<Operation Insert: ' + self.arg2.label + '>'
        elif self.type == self.update:
            return '<Operation Update: ' + self.arg1.label + ' to ' + self.arg2.label + '>'
        else:
            return '<Operation Match: ' + self.arg1.label + ' to ' + self.arg2.label + '>'

    def __eq__(self, other):
        if other is None: return False
        if not isinstance(other, Operation):
            raise TypeError("Must compare against type Operation")
        return self.type == other.type and self.arg1 == other.arg1 and \
            self.arg2 == other.arg2

REMOVE = Operation.remove
INSERT = Operation.insert
UPDATE = Operation.update
MATCH = Operation.match

def tree_edit_distance(A, B, get_children=Node.get_children,
        get_label=Node.get_label, label_dist=strdist, return_operations=False):
    return distance(
        A, B, get_children,
        insert_cost=lambda node: label_dist('', get_label(node)),
        remove_cost=lambda node: label_dist(get_label(node), ''),
        update_cost=lambda a, b: label_dist(get_label(a), get_label(b)),
        return_operations=return_operations
    )

def distance(A, B, get_children, insert_cost, remove_cost, update_cost,
             return_operations=False):
    A, B = AnnotatedTree(A, get_children), AnnotatedTree(B, get_children)
    size_a = len(A.nodes)
    size_b = len(B.nodes)
    treedists = np.zeros((size_a, size_b), float)
    operations = [[[] for _ in range(size_b)] for _ in range(size_a)]

    def treedist(i, j):
        Al = A.lmds
        Bl = B.lmds
        An = A.nodes
        Bn = B.nodes

        m = i - Al[i] + 2
        n = j - Bl[j] + 2
        fd = np.zeros((m,n), float)
        partial_ops = [[[] for _ in range(n)] for _ in range(m)]

        ioff = Al[i] - 1
        joff = Bl[j] - 1

        for x in range(1, m):
            node = An[x+ioff]
            fd[x][0] = fd[x-1][0] + remove_cost(node)
            op = Operation(REMOVE, node)
            partial_ops[x][0] = partial_ops[x-1][0] + [op]
        for y in range(1, n):
            node = Bn[y+joff]
            fd[0][y] = fd[0][y-1] + insert_cost(node)
            op = Operation(INSERT, arg2=node)
            partial_ops[0][y] = partial_ops[0][y-1] + [op]

        for x in range(1, m):
            for y in range(1, n):
                node1 = An[x+ioff]
                node2 = Bn[y+joff]
                if Al[i] == Al[x+ioff] and Bl[j] == Bl[y+joff]:
                    costs = [fd[x-1][y] + remove_cost(node1),
                             fd[x][y-1] + insert_cost(node2),
                             fd[x-1][y-1] + update_cost(node1, node2)]
                    fd[x][y] = min(costs)
                    min_index = costs.index(fd[x][y])

                    if min_index == 0:
                        op = Operation(REMOVE, node1)
                        partial_ops[x][y] = partial_ops[x-1][y] + [op]
                    elif min_index == 1:
                        op = Operation(INSERT, arg2=node2)
                        partial_ops[x][y] = partial_ops[x][y - 1] + [op]
                    else:
                        op_type = MATCH if fd[x][y] == fd[x-1][y-1] else UPDATE
                        op = Operation(op_type, node1, node2)
                        partial_ops[x][y] = partial_ops[x - 1][y - 1] + [op]

                    operations[x + ioff][y + joff] = partial_ops[x][y]
                    treedists[x+ioff][y+joff] = fd[x][y]
                else:
                    p = Al[x+ioff]-1-ioff
                    q = Bl[y+joff]-1-joff
                    costs = [fd[x-1][y] + remove_cost(node1),
                             fd[x][y-1] + insert_cost(node2),
                             fd[p][q] + treedists[x+ioff][y+joff]]
                    fd[x][y] = min(costs)
                    min_index = costs.index(fd[x][y])
                    if min_index == 0:
                        op = Operation(REMOVE, node1)
                        partial_ops[x][y] = partial_ops[x-1][y] + [op]
                    elif min_index == 1:
                        op = Operation(INSERT, arg2=node2)
                        partial_ops[x][y] = partial_ops[x][y-1] + [op]
                    else:
                        partial_ops[x][y] = partial_ops[p][q] + \
                            operations[x+ioff][y+joff]

    for i in A.keyroots:
        for j in B.keyroots:
            treedist(i, j)

    return treedists[-1][-1]


if __name__ == '__main__':
    n1_1 = Node('a', [])
    n1_2 = Node('b', [])
    n1_3 = Node('b', [n1_1, n1_2])
    n1_4 = Node('a', [])
    n1_5 = Node('d', [])
    n1_6 = Node('e', [n1_4, n1_5])
    tree_1 = Node('a', [n1_3, n1_6])

    n2_1 = Node('b', [])
    n2_2 = Node('a', [])
    n2_3 = Node('d', [])
    n2_4 = Node('c', [n2_2, n2_3])
    tree_2 = Node('a', [n2_1, n2_4])

    print(tree_edit_distance(tree_1, tree_2))
