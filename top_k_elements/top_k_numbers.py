

import heapq

class MaxHeap:

    # Initialize the max heap
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)

    # Push item onto max heap, maintaining the heap invariant
    def push(self, item):
        heapq.heappush(self.data, -item)

    # Pop the largest item off the max heap, maintaining the heap invariant
    def pop(self):
        return -heapq.heappop(self.data)

    # Pop and return the current largest value, and add the new item
    def replace(self, item):
        return heapq.heapreplace(self.data, -item)

    # Return the current largest value in the max heap
    def top(self):
        return -self.data[0]


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


