
import heapq
from typing import List


def binary_search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return start

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]: # Verified on Leetcode
    x_index = binary_search(arr, x)

    min_heap = []
    for num in arr[max(x_index - k, 0): min(x_index + k, len(arr) - 1) + 1]:
        min_heap.append((abs(num - x), num))

    heapq.heapify(min_heap)

    result = []
    while len(result) < k:
        _, num = heapq.heappop(min_heap)
        result.append(num)

    return sorted(result)


if __name__ == "__main__":
    print(findClosestElements([1, 1, 1, 10, 10, 10], k=1, x=9))