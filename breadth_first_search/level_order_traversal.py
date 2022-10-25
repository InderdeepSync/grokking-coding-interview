
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root): # Verified on Leetcode
    result = []
    if not root:
        return result

    nodes = [(root, 0)]
    current_level = -1
    while nodes:
        node_to_process, depth = nodes.pop(0)
        if depth == current_level:
            result[-1].append(node_to_process.val)
        else:
            current_level = depth
            result.append([node_to_process.val])

        if node_to_process.left:
            nodes.append((node_to_process.left, depth + 1))
        if node_to_process.right:
            nodes.append((node_to_process.right, depth + 1))
    return result


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(levelOrder(root))