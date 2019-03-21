import node
import tree


def main():
    """Tests postorder (DFS) algorithm on a binary tree.

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
    postorder = t.dfs_postorder_rec_traversal()
    print(postorder)
    postorder = t.dfs_postorder_itr_traversal()
    print(postorder)


if __name__ == "__main__":
    main()
