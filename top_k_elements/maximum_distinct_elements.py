
import heapq

def maximum_distinct_elements (arr, k): # Verified on GeeksForGeeks
    info = {}
    for num in arr:
        if num in info:
            info[num] += 1
        else:
            info[num] = 1

    max_heap = []
    for num, freq in info.items():
        heapq.heappush(max_heap, (-freq, num))


    count_removed = 0
    max_distinct = len(info)
    while count_removed < k:
        if not max_heap:
            return max_distinct - (k - count_removed)
        freq, _ = heapq.heappop(max_heap)
        freq = -1 * freq

        if freq > 1:
            count_removed += freq - 1
        elif freq == 1:
            count_removed += 1
            max_distinct -= 1

    return max_distinct


if __name__ == "__main__":
    print(maximum_distinct_elements([2, 12, 14, 1, 2, 11, 1, 1, 19, 18, 2, 8, 4, 9, 3, 3, 14, 17, 16, 13], 19))