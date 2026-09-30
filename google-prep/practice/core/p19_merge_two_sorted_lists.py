"""
p19. Merge Two Sorted Lists (Easy)
Topic: Linked List

Given the heads of two sorted linked lists, merge them into one sorted
linked list and return its head.

Example:
Input: l1 = 1 -> 2 -> 4, l2 = 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
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


def merge_two_lists(l1, l2):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert list_to_python(merge_two_lists(build_list([1, 2, 4]), build_list([1, 3, 4]))) == [
        1, 1, 2, 3, 4, 4
    ]
    assert list_to_python(merge_two_lists(build_list([]), build_list([]))) == []
    assert list_to_python(merge_two_lists(build_list([]), build_list([0]))) == [0]
    assert list_to_python(merge_two_lists(build_list([5]), build_list([1, 2, 4]))) == [1, 2, 4, 5]
    print("All tests passed!")
