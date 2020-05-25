from anytree import Node, RenderTree

class MyNode(Node):
    def count(self):
        return len(self.descendants) + 1

# class Forest(object):
#     def __init__(self, l, r, index):
#         self.l = l
#         self.r = r
#         self.index = index
#
#     def rightmost_forest(self):
#         r = self.r - 1
#         trace = {r: True}
#         t = r - 1
#         while True:
#             if t < 0: break
#             parent = index[t].parent.v[:index]
#
#     def count(self):
#         return self.r - self.l
#
#     def empty(self):
#         return self.l == self.r
#
# class ForestEditDistance(object):
#     def __init__(self, f1, f2):
#         self.f1, self.f2 = f1, f2
#         self.d = []
#
#     def edit_distance(self):
#         if xforest.empty: return yforest.count
#         if yforest.empty: return xforest.count
#
#         xrtree = xforest.rightmost_forest
#         yrtree = yforest.rightmost_forest


if __name__ == '__main__':
    tree_a = [MyNode('A')]
    tree_a.append(MyNode('B', parent=tree_a[0]))
    tree_a.append(MyNode('C', parent=tree_a[0]))
    tree_a.append(MyNode('A', parent=tree_a[1]))
    tree_a.append(MyNode('B', parent=tree_a[1]))

    for pre, fill, node in RenderTree(tree_a[0]):
        print("%s%s" % (pre, node.name))
    print(tree_a[0].count())

    #
    # tree_b = [Node('A')]
    # tree_b.append(Node('B', parent=tree_b[0]))
    # tree_b.append(Node('C', parent=tree_b[0]))
    # tree_b.append(Node('B', parent=tree_b[1]))
    # tree_b.append(Node('B', parent=tree_b[1]))
    # for pre, fill, node in RenderTree(tree_b[0]):
    #     print("%s%s" % (pre, node.name))
    #
    # print(tree_b[0].is_root)
