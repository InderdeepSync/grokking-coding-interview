class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(val={self.val})"

def min_depth(root): # Verified on Leetcode
    if not root:
        return 0

    nodes = [(root, 1)]

    while nodes:
        node, depth = nodes.pop(0)
        if not node.left and not node.right:
            return depth

        if node.left:
            nodes.append((node.left, depth + 1))
        if node.right:
            nodes.append((node.right, depth + 1))


if __name__ == "__main__":
    tree = TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)))))
    print(min_depth(tree))