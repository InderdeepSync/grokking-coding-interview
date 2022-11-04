"""
https://leetcode.com/problems/different-ways-to-add-parentheses/

"""
from typing import List

operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y}

def diffWaysToCompute(expression: str) -> List[int]: # Accepted ono Leetcode
    if expression.isdigit():
        return [int(expression)]

    index = 0
    result = []
    while index < len(expression):
        if not expression[index].isdigit():
            for way_right in diffWaysToCompute(expression[index + 1:]):
                for way_left in diffWaysToCompute(expression[0: index]):
                    result.append(operations[expression[index]](way_left, way_right))


        index += 1

    return result





if __name__ == "__main__":
    print(diffWaysToCompute("2*3-4*5"))
    # print(diffWaysToCompute("5"))

