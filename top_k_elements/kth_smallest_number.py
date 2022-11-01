
from utils import MaxHeap

def kth_smallest(nums, k):
    max_heap = MaxHeap(nums[:k])

    for num in nums[k:]:
        if num < max_heap.top():
            max_heap.pop()
            max_heap.push(num)

    return max_heap.top()



if __name__ == "__main__":
    print(kth_smallest([1, 5, 12, 2, 11, 5], 3))