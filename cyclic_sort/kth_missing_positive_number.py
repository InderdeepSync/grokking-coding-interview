from typing import List


def findKthPositive(arr: List[int], k: int) -> int: # Verified on Leetcode
    expected = 1
    missing = []
    index = 0
    while index < len(arr):
        if arr[index] == expected:
            expected += 1
            index += 1
        else:
            missing.append(expected)
            expected += 1
            if len(missing) == k:
                return missing[-1]

    return expected + (k - 1 - len(missing))


if __name__ == "__main__":
    print(findKthPositive([1, 2, 3, 4], 2))
