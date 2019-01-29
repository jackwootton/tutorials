import node
import tree


def main():
    """Tests preorder (DFS) algorithm on a binary tree.

    Constructed binary tree is
            A
          /   \
         B     C
        /  \
       D    E
           / \
          F   G
    """
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
    preorder_rec = t.dfs_preorder_rec()
    print(preorder, preorder_rec)


if __name__ == "__main__":
    main()
