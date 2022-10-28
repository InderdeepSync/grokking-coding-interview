
def merge(nums1, m, nums2, n): # Verified on Leetcode
    p1 = 0
    p2 = 0

    number_of_insertions = 0
    while p1 < m + number_of_insertions and p2 < n:
        if nums1[p1] <= nums2[p2]:
            p1 += 1
        else:
            nums1.insert(p1, nums2[p2])
            nums1.pop()
            number_of_insertions += 1
            p2 += 1
            p1 += 1

    if p2 < n:
        nums1[m + n - (n - p2):m + n] = nums2[p2:]


if __name__ == "__main__":
    arr1 = [4, 0, 0, 0, 0, 0]
    arr2 = [1, 2, 3, 5, 6]
    merge(arr1, 1, arr2, 5)
    print(arr1)