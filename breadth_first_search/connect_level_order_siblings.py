class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect(tree_root):
    if tree_root is None:
        return

    nodes = [tree_root]
    prev_node = None
    while nodes:
        current_node = nodes.pop()

        if prev_node:
            prev_node.next = current_node
        prev_node = current_node

        if current_node.left:
            nodes.append(current_node.left)
        if current_node.right:
            nodes.append(current_node.right)


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect(root)
    root.print_tree()
