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

def kth_smallest(nums, k):
    max_heap = MaxHeap(nums[:k])

    for num in nums[k:]:
        if num < max_heap.top():
            max_heap.replace(num)

    return max_heap.top()



if __name__ == "__main__":
    print(kth_smallest([1, 5, 12, 2, 11, 5], 3))