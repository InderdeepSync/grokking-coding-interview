from typing import List


def next_greatest_letter(letters: List[str], target: str) -> str: # Verified on Leetcode
    start = 0
    end = len(letters) - 1

    while start <= end:
        mid = (start + end) // 2

        if ord(letters[mid]) == ord(target):
            temp = mid + 1
            while temp < len(letters):
                if letters[temp] != target:
                    return letters[temp]
                temp += 1

            return letters[0]
        elif ord(letters[mid]) < ord(target):
            start = mid + 1
        else:
            end = mid - 1

    return letters[start] if start < len(letters) else letters[0]


if __name__ == "__main__":
    print(next_greatest_letter(["c", "f", "j"], "a"))