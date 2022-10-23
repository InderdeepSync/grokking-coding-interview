
def make_squares(arr): # Verified on Leetcode
    squares = []
    p1 = -1

    while p1 < len(arr) - 1:
        if arr[p1 + 1] >= 0:
            break
        p1 += 1

    p2 = p1 + 1

    while p1 >= 0 and p2 != len(arr):
        if -1 * arr[p1] < arr[p2]:
            squares.append(arr[p1] * arr[p1])
            p1 -= 1
        else:
            squares.append(arr[p2] * arr[p2])
            p2 += 1

    while p1 >= 0:
        squares.append(arr[p1] * arr[p1])
        p1 -= 1

    while p2 != len(arr):
        squares.append(arr[p2] * arr[p2])
        p2 += 1

    return squares



if __name__ == "__main__":
    print(make_squares([1, 2, 5]))