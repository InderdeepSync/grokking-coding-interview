import math
from typing import List


def min_size_subarray_length(target: int, nums: List[int]) -> int: # Verified on Leetcode
    start, end = 0, 1

    min_length = math.inf
    prev_sum = None
    while end <= len(nums):
        if prev_sum is None:
            current_sum = sum(nums[start: end])
            if current_sum >= target:
                return 1

            end += 1
        else:
            if prev_sum >= target:
                current_sum = prev_sum - nums[start - 1]
            else:
                current_sum = prev_sum + nums[end - 1]

            if current_sum >= target:
                min_length = min(min_length, end - start)
                start += 1
            else:
                end += 1

        prev_sum = current_sum

    return min_length if min_length != math.inf else 0


if __name__ == "__main__":
    print(min_size_subarray_length(7, [2, 3, 1, 2, 4, 3]))
