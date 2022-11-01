import heapq
from typing import List


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

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

    def __iter__(self):
        return iter(self.data)

def medianSlidingWindow(nums: List[int], k: int) -> List[float]: # Accepted on Leetcode
    min_heap = []
    max_heap = MaxHeap()

    def _balance():
        if len(max_heap) == 0 and len(min_heap) != 0:
            max_heap.push(heapq.heappop(min_heap))

        if abs(len(max_heap) - len(min_heap)) <= 1:
            return

        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, max_heap.pop())
        else:
            max_heap.push(heapq.heappop(min_heap))

    def addNum(num: int) -> None:
        if len(max_heap) == 0 or len(min_heap) == 0:
            max_heap.push(num)
        else:
            if num > min_heap[0]:
                heapq.heappush(min_heap, num)
            elif num < max_heap.top():
                max_heap.push(num)
            elif max_heap.top() <= num <= min_heap[0]:
                if len(max_heap) > len(min_heap):
                    heapq.heappush(min_heap, num)
                else:
                    max_heap.push(num)

        _balance()

    def findMedian() -> float:
        if len(max_heap) == len(min_heap):
            return (max_heap.top() + min_heap[0]) / 2

        if len(max_heap) > len(min_heap):
            return max_heap.top()
        else:
            return min_heap[0]

    def removeNum(num_to_remove):
        if -num_to_remove in max_heap:
            max_heap.data.remove(-num_to_remove)
            heapq.heapify(max_heap.data)
        else:
            min_heap.remove(num_to_remove)
            heapq.heapify(min_heap)

        _balance()

    for item in nums[:k - 1]:
        addNum(item)

    result = []
    for index, item in enumerate(nums[k - 1:], start=k - 1):
        addNum(item)
        result.append(findMedian())
        removeNum(nums[index - (k - 1)])

    return result


if __name__ == "__main__":
    print(medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3))
