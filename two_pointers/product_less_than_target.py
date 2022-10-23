from functools import reduce


def find_subarrays(arr, target):
    result = []

    for i in range(len(arr)):
        current_product = 1
        for j in range(i, len(arr)):
            current_product *= arr[j]
            if current_product >= target:
                break

            result.append(arr[i: j + 1])

    return result


if __name__ == "__main__":
    print(print(find_subarrays([2, 5, 3, 10], 30)))
