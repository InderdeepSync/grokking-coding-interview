from typing import List


def search(nums: List[int], target: int) -> int: # Verified on Leetcode
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


if __name__ == "__main__":
    print(search([1, 3, 5, 6], 2))
