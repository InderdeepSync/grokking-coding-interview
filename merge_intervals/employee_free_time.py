
import math
from typing import List, Tuple

import heapq

class ComparableMixin:
    def __eq__(self, other):
        return not self < other and not other < self

    def __ne__(self, other):
        return self < other or other < self

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return not other < self


class Interval(ComparableMixin, object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __getitem__(self, index):
        return self.start if index == 0 else self.end

    def __repr__(self):
        return f"Interval(start={self.start}, end={self.end})"

    def __str__(self):
        return f"[{self.start}, {self.end}]"

    def __lt__(self, other):
        assert(isinstance(other, Interval))

        return self.start <= other.start


def compute_complement(work_hours: List[Interval]):
    free_time = []
    for index, interval in enumerate(work_hours):
        if index == 0:
            free_time.append([-math.inf, interval[0]])
        else:
            free_time.append([work_hours[index - 1][1], interval[0]])

    free_time.append([work_hours[-1][1], math.inf])
    return free_time


def merge_schedule(schedule: List[List[Interval]]):
    min_heap: List[Tuple[Interval, int]] = []

    for employee_index in range(len(schedule)):
        heapq.heappush(min_heap, (schedule[employee_index][0], employee_index))

    merged_intervals = []
    while min_heap:
        interval, employee_index = heapq.heappop(min_heap)
        if not merged_intervals:
            merged_intervals.append(interval)
        else:
            prev_interval = merged_intervals[-1]
            if interval.start <= prev_interval.end:
                merged_intervals[-1] = Interval(prev_interval.start, interval.end)
            else:
                merged_intervals.append(interval)

        schedule[employee_index].pop(0)

        if schedule[employee_index]:
            heapq.heappush(min_heap, (schedule[employee_index][0], employee_index))

    return merged_intervals

def find_employee_free_time(schedule):
    merged_employee_hours = merge_schedule(schedule)
    return compute_complement(merged_employee_hours)[1: -1]


if __name__ == '__main__':
    input1 = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
    # print(input1)
    print("Free intervals: ", find_employee_free_time(input1))

    input2 = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", find_employee_free_time(input2))

    input3 = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    print(find_employee_free_time(input3))
