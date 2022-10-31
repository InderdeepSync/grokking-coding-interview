import heapq

def sumBetweenTwoKth(nums, k1, k2): # Verified on GeeksForGeeks
    max_heap = [-num for num in nums[:k2]]
    heapq.heapify(max_heap)

    for num in nums[k2:]:
        if num < -1 * max_heap[0]:
            heapq.heapreplace(max_heap, -1 * num)

    result = 0

    num_count = 0
    heapq.heappop(max_heap)
    while num_count < k2 - k1 - 1:
        result += -1 * heapq.heappop(max_heap)
        num_count += 1

    return result


if __name__ == "__main__":
    # Sorted => [4, 8, 10, 12, 14, 20, 22]
    print(sumBetweenTwoKth([20, 8, 22, 4, 12, 10, 14], k1=3, k2=6))