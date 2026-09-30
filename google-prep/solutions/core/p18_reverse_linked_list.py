"""
p18. Reverse Linked List (Easy)
Topic: Linked List

Given the head of a singly linked list, reverse the list and return the
new head.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def list_to_python(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


if __name__ == "__main__":
    assert list_to_python(reverse_list(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert list_to_python(reverse_list(build_list([1, 2]))) == [2, 1]
    assert reverse_list(build_list([])) is None
    assert list_to_python(reverse_list(build_list([1]))) == [1]
    print("All tests passed!")
