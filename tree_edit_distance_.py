from anytree import Node, RenderTree

class Forest(object):
    def __init__(self, forest):
        self.forest = forest

    def rightmost_forest(self):
        return f[-1]

    def count(self):
        return self.r - self.l

    def empty(self):
        return self.l == self.r

class ForestEditDistance(object):
    def __init__(self, f1, f2):
        self.f1, self.f2 = f1, f2
        self.d = []

    def edit_distance(self):
        if xforest.empty: return yforest.count
        if yforest.empty: return xforest.count

        xrtree = xforest.rightmost_forest
        yrtree = yforest.rightmost_forest


if __name__ == '__main__':
    tree_a = [Node('A')]
    tree_a.append(Node('B', parent=tree_a[0]))
    tree_a.append(Node('C', parent=tree_a[0]))
    tree_a.append(Node('A', parent=tree_a[1]))
    tree_a.append(Node('B', parent=tree_a[1]))
    for pre, fill, node in RenderTree(tree_a[0]):
        print("%s%s" % (pre, node.name))

    tree_b = [Node('A')]
    tree_b.append(Node('B', parent=tree_b[0]))
    tree_b.append(Node('C', parent=tree_b[0]))
    tree_b.append(Node('B', parent=tree_b[1]))
    tree_b.append(Node('B', parent=tree_b[1]))
    for pre, fill, node in RenderTree(tree_b[0]):
        print("%s%s" % (pre, node.name))

    print(tree_b[0].is_root)
