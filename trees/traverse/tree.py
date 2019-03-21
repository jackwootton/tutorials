class Tree:
    def __init__(self, root=None):
        self.root_node = root

    def bfs_traversal(self):
        visited = []
        node_queue = [self.root_node]

        while len(node_queue):
            current_node = node_queue.pop(0)
            # Record the visit
            visited.append(current_node.value)

            # Left subtree
            if current_node.left_child:
                node_queue.append(current_node.left_child)
            # Right subtree
            if current_node.right_child:
                node_queue.append(current_node.right_child)

        return visited

    def bfs_path(self, destination):
        visited = {}
        node_queue = [(self.root_node, None)]

        while len(node_queue):
            current_node, parent_node = node_queue.pop(0)
            visited[current_node.value] = parent_node
            if current_node.value == destination:
                break

            # Left subtree
            if current_node.left_child:
                left = (current_node.left_child, current_node)
                node_queue.append(left)
            # Right subtree
            if current_node.right_child:
                right = (current_node.right_child, current_node)
                node_queue.append(right)

        path = self.backtrack_from_destination_(visited, destination)
        path.reverse()
        return path

    def backtrack_from_destination_(self, visited, destination):
        if destination not in visited:
            return []

        path = [destination]
        parent = visited.get(destination)
        while parent:
            path.append(parent.value)
            parent = visited.get(parent.value)

        return path

    def dfs_preorder_rec_traversal(self):
        return self.dfs_preorder_rec_traversal_(self.root_node)

    def dfs_preorder_rec_traversal_(self, root_node):
        """Algorithm for preorder traversal
        1. Visit the root node
        2. Traverse the left subtree
        3. Traverse the right subtree
        """
        if root_node is None:
            return []

        # Root node
        visited = [root_node.value]

        # Left subtree
        left_subtree = self.dfs_preorder_rec_traversal_(
            root_node.left_child)
        visited.extend(left_subtree)

        # Right subtree
        right_subtree = self.dfs_preorder_rec_traversal_(
            root_node.right_child)
        visited.extend(right_subtree)

        return visited

    def dfs_preorder_itr_traversal(self):
        """Algorithm for preorder traversal
        1. Visit the root node
        2. Traverse the left subtree
        3. Traverse the right subtree
        """
        node_stack = [self.root_node]
        visited = []

        while len(node_stack):
            current_node = node_stack.pop()
            # Root node
            visited.append(current_node.value)

            # Right subtree (visited *second* because of LIFO)
            if current_node.right_child:
                node_stack.append(current_node.right_child)

            # Left subtree (visited *first* because of LIFO)
            if current_node.left_child:
                node_stack.append(current_node.left_child)

        return visited

    def dfs_inorder_rec_traversal(self):
        return self.dfs_inorder_rec_traversal_(self.root_node)

    def dfs_inorder_rec_traversal_(self, root_node):
        """Algorithm for preorder traversal
        1. Traverse the left subtree
        2. Visit the root node
        3. Traverse the right subtree
        """
        if root_node is None:
            return []

        # Left subtree
        left_subtree = self.dfs_inorder_rec_traversal_(
            root_node.left_child)
        visited = left_subtree

        # Root node
        visited.append(root_node.value)

        # Right subtree
        right_subtree = self.dfs_inorder_rec_traversal_(
            root_node.right_child)
        visited.extend(right_subtree)

        return visited

    def dfs_inorder_itr_traversal(self):
        """Algorithm for preorder traversal
        1. Traverse the left subtree
        2. Visit the root node
        3. Traverse the right subtree
        """
        node_stack = []
        visited = []
        current_node = self.root_node
        while True:
            # Consume left subtree
            if current_node is not None:
                node_stack.append(current_node)
                current_node = current_node.left_child
                continue

            if not len(node_stack):
                break

            current_node = node_stack.pop()
            visited.append(current_node.value)
            # The next iteration will be on the *right* subtree
            current_node = current_node.right_child

        return visited

    def dfs_postorder_rec_traversal(self):
        return self.dfs_postorder_rec_traversal_(self.root_node)

    def dfs_postorder_rec_traversal_(self, root_node):
        """Algorithm for preorder traversal:
        1. Traverse the left subtree
        2. Traverse the right subtree
        3. Visit the root node
        """
        if root_node is None:
            return []

        # Left subtree
        left_subtree = self.dfs_postorder_rec_traversal_(
            root_node.left_child)
        visited = left_subtree

        # Right subtree
        right_subtree = self.dfs_postorder_rec_traversal_(
            root_node.right_child)
        visited.extend(right_subtree)

        # Root node
        visited.append(root_node.value)

        return visited

    def dfs_postorder_itr_traversal(self):
        """Algorithm for preorder traversal
        1. Traverse the left subtree
        2. Traverse the right subtree
        3. Visit the root node
        """
        node_stack = [self.root_node]
        visited = []
        while len(node_stack):
            current_node = node_stack.pop()
            visited.append(current_node.value)

            if current_node.left_child:
                node_stack.append(current_node.left_child)

            if current_node.right_child:
                node_stack.append(current_node.right_child)

        visited.reverse()
        return visited
