from typing import List
import heapq

from utils import MaxHeap

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
    print(findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))
