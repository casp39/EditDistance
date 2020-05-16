from anytree import Node, RenderTree



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
