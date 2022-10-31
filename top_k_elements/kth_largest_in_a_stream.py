import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums[:k]
        heapq.heapify(self.min_heap)
        for num in nums[k:]:
            if num > self.min_heap[0]:
                heapq.heapreplace(self.min_heap, num)

        self.k = k

    def add(self, val: int) -> int:
        if val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)

        return self.min_heap[0]


if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    param_1 = obj.add(3)
    print(param_1)