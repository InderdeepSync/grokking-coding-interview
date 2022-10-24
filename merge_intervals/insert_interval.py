def merge_overlapping_intervals(intervals):
    intervals.sort(key=lambda item: item[0])
    merged_intervals = [intervals[0]]

    for index in range(1, len(intervals)):
        prev_interval = merged_intervals[-1]
        current_interval = intervals[index]

        if prev_interval[1] < current_interval[0]:
            merged_intervals.append(current_interval)
        else:
            merged_interval = [prev_interval[0], max(current_interval[1], prev_interval[1])]
            merged_intervals[-1] = merged_interval

    return merged_intervals


def insert(intervals, new_interval): # Verified on Leetcode
    o_start, o_end = 0, 0

    for index, interval in enumerate(intervals):
        if new_interval[0] > interval[1]:
            o_start += 1

        o_end += 1

    intervals[o_start: o_end] = merge_overlapping_intervals([new_interval, *intervals[o_start: o_end]])

    return intervals


if __name__ == "__main__":
    # print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    # print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print(insert([[3, 5], [12, 15]], [6, 6]))
