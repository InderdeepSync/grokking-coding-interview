

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root): # Verified on Leetcode
    result = []
    if not root:
        return result

    nodes = [(root, 0)]
    current_level = -1
    direction = False
    while nodes:
        node_to_process, depth = nodes.pop(0)
        if depth == current_level:
            if direction:
                result[-1].append(node_to_process.val)
            else:
                result[-1].insert(0, node_to_process.val)
        else:
            current_level = depth
            direction = not direction
            result.append([node_to_process.val])

        if node_to_process.left:
            nodes.append((node_to_process.left, depth + 1))
        if node_to_process.right:
            nodes.append((node_to_process.right, depth + 1))
    return result






if __name__ == "__main__":
    tree = TreeNode(12)
    tree.left = TreeNode(7)
    tree.right = TreeNode(1)
    tree.left.left = TreeNode(9)
    tree.right.left = TreeNode(10)
    tree.right.right = TreeNode(5)
    tree.right.left.left = TreeNode(20)
    tree.right.left.right = TreeNode(17)
    print(zigzag_level_order(tree))