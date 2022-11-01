
import heapq

from utils import MaxHeap

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



