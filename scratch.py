#! /usr/bin/python
from typing import List, Optional
from pprint import pprint


def reverseVowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    end = len(s) - 1
    start = 0

    result = list(s)
    while start < end:
        while result[end] not in vowels and end > 0:
            end -= 1

        while result[start] not in vowels and start < len(s) - 1:
            start += 1

        if start >= end:
            break

        result[start], result[end] = result[end], result[start]
        start += 1
        end -= 1

    return "".join(result)


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"ListNode({self.val}, {self.next})"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def oddEvenList(head):  # Verified on Leetcode
    if not head or not head.next:
        return head

    end = head

    while end.next and end.next.next:
        end = end.next.next

    prev = head
    even = temp = ListNode("#", head)
    while prev and prev.next:
        current = prev.next

        temp.next = current
        temp = temp.next

        prev.next = current.next
        prev = current.next
        current.next = None

    end.next = even.next

    return head


def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:  # Verified on Leetcode
    slow = fast = head
    prev_slow = result = ListNode("#", head)

    for _ in range(k - 1):
        fast = fast.next

    count = 0
    current = head
    temp1 = result
    while current:
        count += 1
        if count == k - 1:
            temp1 = current
            break

        current = current.next

    while fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next

    temp2 = prev_slow

    t = temp1.next.val
    temp1.next.val = temp2.next.val
    temp2.next.val = t

    return result.next


def spiralMatrix(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:  # Verified on Leetcode
    matrix = [[-1 for _ in range(n)] for _ in range(m)]

    left = -1
    right = n - 1
    top = 0
    bottom = m - 1

    current = head
    row, column = 0, 0
    while current:
        print(row, column)
        matrix[row][column] = current.val
        current = current.next
        if row == top:
            if column < right:
                column += 1
            elif column == right:
                row += 1
                left += 1
        elif column == right:
            if row < bottom:
                row += 1
            elif row == bottom:
                column -= 1
                top += 1
        elif row == bottom:
            if column > left:
                column -= 1
            elif column == left:
                row -= 1
                right -= 1

        elif column == left:
            if row > top:
                row -= 1
                if row == top:
                    bottom -= 1
            elif row == top:
                column += 1

    return matrix


def convertArrToLinkedList(arr):
    prev = result = ListNode("#")
    for num in arr:
        prev.next = ListNode(num)
        prev = prev.next

    return result.next


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:  # Verified on Leetcode
    if target == 0:
        return [[]]

    result = []
    if not candidates:
        return result

    index = 0
    while (targetToAchieve := target - index * candidates[-1]) >= 0:
        temp = combinationSum(candidates[: -1], targetToAchieve)
        result.extend([*[candidates[-1]] * index, *combination] for combination in temp)
        index += 1

    return result


def combine(n: int, k: int) -> List[List[int]]:
    result = [{i} for i in range(1, n + 1)]
    all_numbers = set(range(1, n + 1))

    for i in range(1, k):
        temp = []
        for combination in result:
            allowed = all_numbers - combination
            for num in allowed:
                temp2 = combination.copy()
                temp2.add(num)
                temp.append(temp2)

        result = temp

    return result


def getListMid(head):
    slow = fast = head
    prev_slow = None
    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next

    return prev_slow, slow


def maxProfit(prices: List[int]) -> int:
    possibilities = [(None, 0)]

    for price in prices:
        temp = []
        for possibility in possibilities:
            temp.append(possibility)
            if possibility[0] is None:
                temp.append((price, possibility[1]))
            else:
                temp.append((None, possibility[1] + price - possibility[0]))

        possibilities = temp

    possibilities.sort(key=lambda x: x[1])

    return max(possibilities[-1][1], 0)


def summaryRanges(nums: List[int]):
    start = end = 0

    index = 0

    result = []
    while index < len(nums):
        if start == end:
            end += 1
        elif nums[index] == nums[index - 1] + 1:
            end += 1
        else:
            result.append((nums[start], nums[end - 1]))
            start = end = index
            continue

        index += 1

    return result


if __name__ == "__main__":
    list2 = convertArrToLinkedList(
        [515, 942, 528, 483, 20, 159, 868, 999, 474, 320, 734, 956, 12, 124, 224, 252, 909, 732])
    # pprint(spiralMatrix(4, 5, list2))
    # expected = [[515,942,528,483,20],[124,224,252,909,159],[12,-1,-1,732,868],[956,734,320,474,999]]
    # print(combinationSum([1, 2, 3], 5))
    # list3 = convertArrToLinkedList([1, 2, 3, 4, 5])

    # print(maxProfit([2, 1, 2, 0, 1]))

    # print(summaryRanges([0, 1, 2, 4, 5, 7]))
