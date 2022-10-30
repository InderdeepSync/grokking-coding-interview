import math
from typing import List


def _find_maximum_element(nums, start, end): # Accepted on Leetcode
    while start <= end:
        mid = (start + end) // 2

        prev_element = nums[mid - 1] if mid != 0 else -math.inf
        next_element = nums[mid + 1] if mid != len(nums) - 1 else -math.inf
        if prev_element < nums[mid] < next_element:
            start = mid + 1
        elif prev_element > nums[mid] > next_element:
            end = mid - 1
        elif nums[mid] > prev_element and nums[mid] > next_element:
            return mid
        else:
            return _find_maximum_element(nums, start, mid - 1) or _find_maximum_element(nums, mid + 1, end)
    return None

def find_peak_element(nums: List[int]) -> int:
    return _find_maximum_element(nums, start=0, end=len(nums) - 1)



if __name__ == "__main__":
    print(find_peak_element([1]))