

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def possible_paths(root): # Verified on Leetcode
    if not root:
        return []

    if not root.left and not root.right:
        return [(root.val, 0)]

    possible_sums = []
    for path_sum, height in possible_paths(root.left) + possible_paths(root.right):
        possible_sums.append((pow(10, height + 1) * root.val + path_sum, height + 1))

    return possible_sums


def sum_numbers(root) -> int:
    if not root:
        return 0

    return sum(map(lambda x: x[0], possible_paths(root)))


if __name__ == "__main__":
    head = TreeNode(4)
    head.left = TreeNode(5)
    # head.left.right = TreeNode(2)
    # head.left.left = TreeNode(3)
    # head.right.left = TreeNode(6)
    # head.right.right = TreeNode(5)
    print(sum_numbers(head))
