from typing import List
import math

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"ListNode(value={self.value}, next={repr(self.next)})"

def merge_lists(lists: List[ListNode]): # Verified on Leetcode but very inefficient
    result = current = ListNode("X")
    while True:
        min_value = math.inf
        min_index = None
        for index, pointer in enumerate(lists):
            if not pointer:
                continue
            if pointer.value < min_value:
                min_value = pointer.value
                min_index = index

        if min_index is None:
            break

        current.next = lists[min_index]
        lists[min_index] = lists[min_index].next

        current = current.next
        current.next = None


    return result.next





if __name__ == "__main__":
    list1 = ListNode(2)
    list1.next = ListNode(6)
    list1.next.next = ListNode(8)

    list2 = ListNode(3)
    list2.next = ListNode(6)
    list2.next.next = ListNode(7)

    list3 = ListNode(1)
    list3.next = ListNode(3)
    list3.next.next = ListNode(4)
    merged_list = merge_lists([list1, list2, list3])

    print(merged_list)
