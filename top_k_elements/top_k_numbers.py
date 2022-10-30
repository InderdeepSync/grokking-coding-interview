

import heapq


def top_k_numbers(nums, k): # Verified on Leetcode
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return min_heap


if __name__ == "__main__":
    print(top_k_numbers([5, 12, 11, -1, 12], 3))


