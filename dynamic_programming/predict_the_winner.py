from typing import List


def inner(arr, curScore1, curScore2, turn):
    if len(arr) == 1:
        return curScore1 + arr[0] * turn >= curScore2

    if turn == 1:
        return inner(arr[:-1], curScore1 + arr[-1], curScore2, turn * -1) or inner(arr[1:],
                                                                                   curScore1 + arr[0],
                                                                                   curScore2, turn * -1)
    else:
        return inner(arr[:-1], curScore1, curScore2 + arr[-1], turn * -1) or inner(arr[1:], curScore1,
                                                                                   curScore2 + arr[0],
                                                                                   turn * -1)


def predictTheWinner(nums: List[int]) -> bool:
    return inner(nums, 0, 0, 1)


if __name__ == "__main__":
    print(predictTheWinner([1, 5, 2]))
