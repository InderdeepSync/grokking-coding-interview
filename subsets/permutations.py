from typing import List


def permute(nums: List[int]) -> List[List[int]]: # Verified on Leetcode
    permutations = [[nums[0]]]

    for i in range(1, len(nums)):
        temp = []

        for permutation in permutations:
            for index in range(len(permutation) + 1):
                permutation_copy = permutation[:]
                permutation_copy.insert(index, nums[i])
                temp.append(permutation_copy)

        permutations = temp

    return permutations



if __name__ == "__main__":
    print(permute([1, 2, 3]))