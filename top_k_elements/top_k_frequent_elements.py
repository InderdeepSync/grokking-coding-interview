import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]: # Verified on Leetcode
    frequencies = {}
    for num in nums:
        if num not in frequencies:
            frequencies[num] = 1
        else:
            frequencies[num] += 1

    temp = []
    for num, f in frequencies.items():
        temp.append((f, num))

    min_heap = temp[:k]
    heapq.heapify(min_heap)

    for item in temp[k:]:
        if item[0] > min_heap[0][0]:
            heapq.heapreplace(min_heap, item)

    return list(map(lambda x: x[1], min_heap))


if __name__ == "__main__":
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))