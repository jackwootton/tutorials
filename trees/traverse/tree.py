class Tree:
    def __init__(self, root=None):
        self.root_node = root

    def bfs(self):
        visited = []
        next_nodes = [self.root_node]

        while len(next_nodes):
            current_node = next_nodes.pop(0)

            # Record the visit
            visited.append(current_node.value)

            # Traverse left subtree (later)
            if current_node.left_child:
                next_nodes.append(current_node.left_child)

            # Traverse right subtree (a little later)
            if current_node.right_child:
                next_nodes.append(current_node.right_child)

        return visited

    def dfs_preorder(self):
        """Algorithm for preorder traversal
        1. Visit the root node.
        2. Traverse the left subtree.
        3. Traverse the right subtree.
        """
        visited = []
        next_nodes = [self.root_node]

        while len(next_nodes):
            current_node = next_nodes.pop()

            # Record the visit
            visited.append(current_node.value)

            # Traverse right substree (very soon)
            if current_node.right_child:
                next_nodes.append(current_node.right_child)

            # Traverse left subtree (very soon)
            if current_node.left_child:
                next_nodes.append(current_node.left_child)

        return visited

    def dfs_preorder_rec(self):
        return self.dfs_preorder_helper(self.root_node)

    def dfs_preorder_helper(self, current_node):
        # recursive base case
        if current_node is None:
            return []

        # Visit the root
        visited = [current_node.value]

        # Traverse left subtree (progress toward base case)
        left_subtree = self.dfs_preorder_helper(current_node.left_child)
        visited.extend(left_subtree)

        # Traverse right subtree (progress toward base case)
        right_subtree = self.dfs_preorder_helper(current_node.right_child)
        visited.extend(right_subtree)

        return visited

    def dfs_inorder(self):
        visited = []
        next_nodes = [self.root_node]
        done = False
        # Start at the root node
        current_node = self.root_node

        while not done:
            if current_node:
                # Navigate to the left-most node
                next_nodes.append(current_node)
                current_node = current_node.left_child
            else:
                done = len(next_nodes) < 1
                if not done:
                    # Visit the node
                    current_node = next_nodes.pop()
                    visited.append(current_node.value)

                    # Traverse the right subtree
                    current_node = current_node.right_child

        return visited

    def dfs_postorder(self):
        visited = []
        next_nodes = [self.root_node]
        done = False
        # Start at the root node
        current_node = self.root_node

        while not done:
            if current_node:
                next_nodes.append(current_node)
                current_node = current_node.left_child

            else:
                current_node = current_node.right_child
                done = len(next_nodes) < 1

                current_node = next_nodes.pop()
                visited.append(current_node.value)
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
