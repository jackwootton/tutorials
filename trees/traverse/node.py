class Node:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.visited = False

    def set_children(self, left_child=None, right_child=None):
        self.left_child = left_child
        self.right_child = right_child
