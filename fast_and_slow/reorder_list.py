class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


def reverse(list_head, prev=None):
    cur = list_head

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev

def reorder_linked_list(linked_list): # Verified on Leetcode
    if not linked_list.next:
        return linked_list

    slow = fast = linked_list
    prev_slow = None

    while fast and fast.next:
        fast = fast.next.next
        prev_slow = slow
        slow = slow.next

    list2 = reverse(prev_slow.next)

    prev_slow.next = None
    result = linked_list
    while linked_list:
        temp = linked_list.next
        linked_list.next = list2

        temp2 = list2.next
        list2.next = temp
        list2 = temp2

        if not temp and list2:
            linked_list.next.next = list2

        linked_list = temp


    return result








if __name__ == "__main__":
    head = Node(1)
    # head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)

    reorder_linked_list(head)