from typing import List


def generateParenthesis(n: int) -> List[str]: # Verified on Leetcode
    result = [""]

    for i in range(n):
        temp = []
        for permutation in result:
            new_permutation = permutation + "("
            close_allowed = new_permutation.count("(") - new_permutation.count(")")

            for j in range(close_allowed + 1):
                temp.append(new_permutation + ")" * j)


        result = temp

    return list(filter(lambda x: len(x) == 2 * n, result))


if __name__ == "__main__":
    print(generateParenthesis(3))