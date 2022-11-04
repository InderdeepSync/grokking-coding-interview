from typing import List

import heapq

def kthSmallest(matrix: List[List[int]], k: int) -> int: # Accepted on Leetcode
    min_heap = []

    for index, row in enumerate(matrix):
        heapq.heappush(min_heap, (row[0], index))

    result = []
    pointers = [0] * len(matrix)
    while min_heap and len(result) < k:
        value, row_index = heapq.heappop(min_heap)
        result.append(value)
        pointers[row_index] += 1

        if pointers[row_index] < len(matrix[row_index]):
            heapq.heappush(min_heap, (matrix[row_index][pointers[row_index]], row_index))

    return result[-1]





if __name__ == "__main__":
    print(kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
