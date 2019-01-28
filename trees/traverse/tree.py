class Tree:
    def __init__(self, root=None):
        self.root_node = root

    def bfs(self):
        traversal = []
        next_nodes = [self.root_node]

        while len(next_nodes):
            current_node = next_nodes[-1]

            # Visit the root
            current_node.visited = True
            traversal.append(current_node.value)
            next_nodes.pop()

            # Traverse left subtree
            lc = current_node.left_child
            if lc and not lc.visited:
                next_nodes.insert(0, lc)

            # Traverse right subtree
            rc = current_node.right_child
            if rc and not rc.visited:
                next_nodes.insert(0, rc)

        return traversal

    def dfs_preorder(self):
        """Algorithm preorder
        1. Visit the root.
        2. Traverse the left subtree
        3. Traverse the right subtree
        """
        traversal = []
        next_nodes = [self.root_node]

        while len(next_nodes):
            current_node = next_nodes[-1]

            # Visit the root
            current_node.visited = True
            traversal.append(current_node.value)
            next_nodes.pop()

            # Traverse right substree
            rc = current_node.right_child
            if rc and not rc.visited:
                next_nodes.append(rc)

            # Traverse left subtree
            lc = current_node.left_child
            if lc and not lc.visited:
                next_nodes.append(lc)

        return traversal

    def dfs_preorder_rec(self):
        return self.dfs_preorder_helper_(self.root_node)

    def dfs_preorder_helper_(self, current_node):
        """Algorithm dfs_preorder_helper_(tree)
        1. Visit the root.
        2. Traverse the left subtree, i.e. dfs_preorder_helper_(left-subtree)
        3. Traverse the right subtree, i.e. dfs_preorder_helper_(right-subtree)
        """
        if current_node is None:
            return []

        # Visit the root
        current_node.visited = True
        traversal = [current_node.value]

        # Traverse left subtree
        left_subtree = self.dfs_preorder_helper_(current_node.left_child)
        traversal.extend(left_subtree)

        # Traverse right subtree
        right_subtree = self.dfs_preorder_helper_(current_node.right_child)
        traversal.extend(right_subtree)

        return traversal

    def dfs_inorder(self):
        """Algorithm inorder
        1. Traverse the left subtree
        2. Visit the root
        3. Traverse the right subtree
        """
        traversal = []
        next_nodes = [self.root_node]

        while len(next_nodes):
            current_node = next_nodes[-1]

            # Traverse left subtree
            lc = current_node.left_child
            if lc and not lc.visited:
                next_nodes.append(lc)
                continue

            # Visit the root
            current_node.visited = True
            traversal.append(current_node.value)
            next_nodes.pop()

            # Traverse the right subtree
            rc = current_node.right_child
            if rc and not rc.visited:
                next_nodes.append(rc)
                continue

        return traversal

    def dfs_postorder(self):
        """Algorithm postorder
        1. Traverse the left subtree
        2. Traverse the right subtree
        3. Visit the root
        """
        traversal = []
        next_nodes = [self.root_node]

        while len(next_nodes):
            current_node = next_nodes[-1]

            # Traverse left subtree
            lc = current_node.left_child
            if lc and not lc.visited:
                next_nodes.append(lc)
                continue

            # Traverse the right subtree
            rc = current_node.right_child
            if rc and not rc.visited:
                next_nodes.append(rc)
                continue

            # Visit the root
            current_node.visited = True
            traversal.append(current_node.value)
            next_nodes.pop()

        return traversal
