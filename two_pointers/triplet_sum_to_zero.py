def search_triplets(arr):
    arr.sort()

    triplets = []
    for i in range(len(arr) - 2):
        lower = i + 1
        upper = len(arr) - 1
        while lower < upper:
            if arr[lower] + arr[upper] == -1 * arr[i]:
                triplets.append([arr[i], arr[lower], arr[upper]])
                lower += 1
                upper -= 1
            elif arr[lower] + arr[upper] > -1 * arr[i]:
                upper -= 1
            else:
                lower += 1

    return triplets



def findTriplets(arr):
    """
    :param arr:
    :return: True if at least one triplet exists
    """
    arr.sort()

    index = -1
    while arr[index + 1] < 0:
        index += 1

    for i in range(len(arr)):
        start, end = (index + 1, len(arr) - 1) if i <= index else (0, index)
        target_sum = -1 * arr[i]

        while start < end:
            current_sum = arr[start] + arr[end]
            if current_sum == target_sum:
                return True
            elif current_sum < target_sum:
                start += 1
            else:
                end -= 1

    return False


if __name__ == "__main__":
    print(findTriplets([4, -24, 34, -35, 60, -24, 72, 18, 97, -54, 12, -81, 13, -43]))