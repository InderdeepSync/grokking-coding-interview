import math


def backspaceCompare(str1: str, str2: str) -> bool: # Verified on Leetcode
    p1 = len(str1) - 1
    p2 = len(str2) - 1
    while p1 >= 0 and p2 >= 0:
        while p1 >= 0 and str1[p1] == "#":
            temp = 0
            while str1[p1 - temp] == "#":
                temp += 1

            upper = p1 - temp + 1
            lower = upper - temp
            while "#" in str1[lower: upper]:
                temp += str1[lower: upper].count("#")
                upper = lower
                lower = max(p1 - 2 * temp + 1, 0)

            p1 -= 2 * temp

        while p2 >= 0 and str2[p2] == "#":
            temp = 0
            while str2[p2 - temp] == "#":
                temp += 1

            upper = p2 - temp + 1
            lower = upper - temp
            while "#" in str2[lower: upper]:
                temp += str2[lower: upper].count("#")
                upper = lower
                lower = max(p2 - 2 * temp + 1, 0)

            p2 -= 2 * temp

        if p1 >= 0 > p2 or p1 < 0 <= p2:
            return False

        if p1 >= 0 and p2 >= 0 and str2[p2] != str1[p1]:
            return False

        p2 -= 1
        p1 -= 1

    return p1 < 0 and p2 < 0 or \
        p1 < 0 and str2[:p2 + 1].count("#") == math.ceil(len(str2[:p2 + 1]) / 2) or \
        p2 < 0 and str1[:p1 + 1].count("#") == math.ceil(len(str1[:p1 + 1]) / 2)


if __name__ == "__main__":
    input1 = "nz"
    input2 = "b#nz"

    print(backspaceCompare(input1, input2))
