import node
import tree


def main():
    a = node.Node('A')
    b = node.Node('B')
    c = node.Node('C')
    d = node.Node('D')
    e = node.Node('E')
    f = node.Node('F')
    g = node.Node('G')

    e.set_children(f, g)
    b.set_children(d, e)
    a.set_children(b, c)

    t = tree.Tree(root=a)
    preorder = t.dfs_preorder()
    print(preorder)


if __name__ == "__main__":
    main()
