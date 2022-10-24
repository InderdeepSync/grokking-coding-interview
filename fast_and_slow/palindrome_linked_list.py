def compare_linked_lists(list1, list2):
    while list1 and list2:
        if list1.val != list2.val:
            return False

        list1 = list1.next
        list2 = list2.next

    return not list1 and not list2


def reverse(list_head, prev=None):
    cur = list_head

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


def is_palindrome(head_node): # Verified on leetcode
    slow = fast = head_node
    prev_slow = None

    while fast and fast.next:
        fast = fast.next.next

        temp1 = prev_slow
        prev_slow = slow
        temp2 = slow.next
        slow.next = temp1
        slow = temp2

    result = compare_linked_lists(prev_slow, slow.next if fast else slow)
    reverse(prev_slow, prev=slow)

    return result


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    # head.next.next.next.next = Node(1)

    print(is_palindrome(head))
