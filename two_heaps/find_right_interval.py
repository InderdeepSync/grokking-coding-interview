from typing import List
from utils import MaxHeap

def findRightInterval(intervals: List[List[int]]) -> List[int]:
    temp = []
    for index, interval in enumerate(intervals):
        temp.append((interval, index))
    intervals = temp
    intervals.sort(key=lambda x: x[0][0])

    result = [-1] * len(intervals)
    for index, interval in enumerate(intervals):
        if index == len(intervals) - 1:
            break

        temp = index + 1
        # next_interval = intervals[index + 1]
        while temp < len(intervals) and intervals[temp][0][0] < interval[0][1]:
            temp += 1

        if temp < len(intervals):
            _, original_index = intervals[temp]
            result[interval[1]] = original_index

    return result


def findRightIntervalEfficient(intervals: List[List[int]]) -> List[int]: # Accepted on Leetcode
    max_start_heap = MaxHeap()
    max_end_heap = MaxHeap()

    for index, interval in enumerate(intervals):
        max_start_heap.push((interval[0], index))
        max_end_heap.push((interval[1], index))

    result = [-1] * len(intervals)
    while max_end_heap:
        interval_end, interval_index = max_end_heap.pop()

        temp = None
        while max_start_heap and max_start_heap.top()[0] >= interval_end:
            temp = max_start_heap.pop()[1]

        if temp is not None:
            result[interval_index] = temp
            max_start_heap.push((intervals[temp][0], temp))

    return result


if __name__ == "__main__":
    print(findRightIntervalEfficient([[3, 4], [2, 3], [1, 2]]))
