
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

    def __len__(self):
        return len(self.data)

class MedianFinder: # Verified on Leetcode
    def _balance(self):
        if abs(len(self.max_heap) - len(self.min_heap)) <= 1:
            return

        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, self.max_heap.pop())
        else:
            self.max_heap.push(heapq.heappop(self.min_heap))


    def __init__(self):
        self.max_heap = MaxHeap()
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0 or len(self.min_heap) == 0:
            self.max_heap.push(num)
        else:
            if num > self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
            elif num < self.max_heap.top():
                self.max_heap.push(num)
            elif self.max_heap.top() <= num <= self.min_heap[0]:
                if len(self.max_heap) > len(self.min_heap):
                    heapq.heappush(self.min_heap, num)
                else:
                    self.max_heap.push(num)

        self._balance()

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap.top() + self.min_heap[0])/2

        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap.top()
        else:
            return self.min_heap[0]



if __name__ == "__main__":
    medianOfAStream = MedianFinder()
    medianOfAStream.addNum(3)
    medianOfAStream.addNum(1)
    print("The median is: " + str(medianOfAStream.findMedian()))
    medianOfAStream.addNum(5)
    print("The median is: " + str(medianOfAStream.findMedian()))
    medianOfAStream.addNum(4)
    print("The median is: " + str(medianOfAStream.findMedian()))



