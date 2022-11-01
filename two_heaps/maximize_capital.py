from typing import List
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
        if isinstance(item, tuple):
            item = (-1 * item[0], item[1])
        heapq.heappush(self.data, item)

    # Pop the largest item off the max heap, maintaining the heap invariant
    def pop(self):
        item = heapq.heappop(self.data)
        return -1 * item[0], item[1]

    # Pop and return the current largest value, and add the new item
    def replace(self, item):
        return heapq.heapreplace(self.data, -item)

    # Return the current largest value in the max heap
    def top(self):
        item = -self.data[0]
        return -1 * item[0], item[1]

    def __len__(self):
        return len(self.data)


def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int: # Accepted on Leetcode
    max_heap = MaxHeap()
    min_heap = []
    for index, capital_i in enumerate(capital):
        min_heap.append((capital_i, index))

    heapq.heapify(min_heap)

    current_capital = w
    for _ in range(k):
        while min_heap and min_heap[0][0] <= current_capital:
            _, project_index = heapq.heappop(min_heap)
            max_heap.push((profits[project_index], project_index))

        if len(max_heap) > 0:
            current_capital += max_heap.pop()[0]

    return current_capital


if __name__ == "__main__":
    print(findMaximizedCapital(k=1, w=0, profits=[1, 2, 3], capital=[1, 1, 2]))
