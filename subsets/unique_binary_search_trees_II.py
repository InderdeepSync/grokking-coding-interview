"""
https://leetcode.com/problems/unique-binary-search-trees-ii/
"""


from typing import List

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_trees_from_numbers(nums): # Accepted on Leetcode
    result = []

    for index in range(len(nums)):
        left_trees = generate_trees_from_numbers(nums[: index]) if index != 0 else [None]
        right_trees = generate_trees_from_numbers(nums[index + 1:]) if index != len(nums) - 1 else [None]

        for tree_left in left_trees:
            for tree_right in right_trees:
                result.append(TreeNode(nums[index], tree_left, tree_right))

    return result




def generateTrees(n: int) -> List[TreeNode]:
    result = generate_trees_from_numbers([i for i in range(1, n + 1)])
    return result





if __name__ == "__main__":
    print(generateTrees(2))
