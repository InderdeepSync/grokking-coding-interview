import heapq
from typing import List


def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]: # Accepted on Leetcode
    max_heap = []

    for value1 in nums1[:min(k, len(nums1))]:
        for value2 in nums2[:min(k, len(nums2))]:
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-1 * value1 - value2, (value1, value2)))
            elif value1 + value2 < -1 * max_heap[0][0]:
                heapq.heapreplace(max_heap, (-1 * value1 - value2, (value1, value2)))
            else:
                break

    pairs = []
    while max_heap and len(pairs) < k:
        min_sum, pair = heapq.heappop(max_heap)
        pairs.append(pair)

    return pairs




if __name__ == "__main__":
    print(kSmallestPairs([1, 2], [3], k=3))
