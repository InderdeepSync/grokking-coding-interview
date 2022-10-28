
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next

        return result

    def __repr__(self):
        return f"ListNode(val={self.val}, next={repr(self.next)})"

def reverse(head_node, prev=None):
    current = head_node
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev


def reverse_k(head, k): # Verified on Leetcode
    result = prev = current = ListNode("X", head)

    while True:
        try:
            for i in range(k):
                current = current.next
            if not current:
                break
        except AttributeError:
            break

        temp = current.next
        current.next = None
        temp2 = prev.next
        prev.next = reverse(prev.next, temp)

        prev = current = temp2

    return result.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)

    reversed_list = reverse_k(head, 3)
    print(reversed_list)
