class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sums(root): # Verified on Leetcode
    possible_sums = []
    if not root.left and not root.right:
        possible_sums.append(root.val)
    else:
        if root.left:
            possible_sums.extend([root.val + path_sum for path_sum in path_sums(root.left)])
        if root.right:
            possible_sums.extend([root.val + path_sum for path_sum in path_sums(root.right)])

    return possible_sums


def has_path_sum(root, target_sum):
    if not root:
        return False

    return target_sum in path_sums(root)

def all_paths(root):
    possible_paths = []

    if not root.left and not root.right:
        possible_paths.append(str(root.val))
    else:
        if root.left:
            possible_paths.extend([f"{root.val}->{path}" for path in all_paths(root.left)])
        if root.right:
            possible_paths.extend([f"{root.val}->{path}" for path in all_paths(root.right)])

    return possible_paths


if __name__ == "__main__":
    head = Node(12)
    head.left = Node(7)
    head.right = Node(1)
    head.left.left = Node(9)
    head.right.left = Node(10)
    head.right.right = Node(5)
    print(all_paths(head))
