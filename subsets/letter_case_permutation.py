from typing import List


def letterCasePermutation(s: str) -> List[str]: # Verified on Leetcode
    result = [""]

    for ch in s:
        temp = []
        for permutation in result:
            if ch.isalpha():
                temp.extend([permutation + ch.lower(), permutation + ch.upper()])
            else:
                temp.append(permutation + ch)

        result = temp

    return result



if __name__ == "__main__":
    print(letterCasePermutation("a1b2"))
