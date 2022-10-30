
def findKRotation(arr): # Verified on GeeksForGeeks
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        prev_index = (mid - 1) % len(arr)
        next_index = (mid + 1) % len(arr)

        if arr[mid] <= arr[prev_index] and arr[mid] <= arr[next_index]:
            return mid
        elif arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[mid] >= arr[low]:
            low = mid + 1
    return 0


if __name__ == "__main__":
    print(findKRotation([5, 1, 2, 3, 4]))