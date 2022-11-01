
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def all_sums(node): # Accepted on Leetcode
    if not node.left and not node.right:
        return [], [node.val]

    sums_excluding_node = []
    sums_including_node = []
    if node.left:
        sums_excluding_child_node, sums_including_child_node = all_sums(node.left)
        sums_excluding_node.extend(sums_excluding_child_node)
        sums_including_node.extend(sums_including_child_node)
    if node.right:
        sums_excluding_child_node, sums_including_child_node = all_sums(node.right)
        sums_excluding_node.extend(sums_excluding_child_node)
        sums_including_node.extend(sums_including_child_node)

    sums_excluding_node.extend(sums_including_node)
    for index in range(len(sums_including_node)):
        sums_including_node[index] += node.val

    sums_including_node.append(node.val)

    return sums_excluding_node, sums_including_node


def pathSum(root, targetSum):
    if not root:
        return 0

    p1, p2 = all_sums(root)
    print(p1, p2)
    return p1.count(targetSum) + p2.count(targetSum)


if __name__ == "__main__":
    tree_root = TreeNode(12)
    tree_root.left = TreeNode(7)
    tree_root.right = TreeNode(1)
    tree_root.left.left = TreeNode(4)
    # tree_root.right.left = TreeNode(10)
    # tree_root.right.right = TreeNode(5)

    print(pathSum(tree_root, 11))