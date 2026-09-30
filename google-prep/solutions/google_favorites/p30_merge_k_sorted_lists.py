"""
p30. Merge K Sorted Lists (Hard)
Topic: Heaps / Linked List
Known as a frequently-asked Google interview question.

Given a list of k sorted linked lists, merge them into a single sorted
linked list and return its head.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
"""

import heapq


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


def merge_k_lists(lists):
    heap = []
    counter = 0  # tiebreaker so heapq never compares ListNode objects directly
    for node in lists:
        if node:
            heapq.heappush(heap, (node.val, counter, node))
            counter += 1

    dummy = ListNode()
    cur = dummy
    while heap:
        _, _, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    return dummy.next


if __name__ == "__main__":
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    assert list_to_python(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_lists([]) is None
    assert merge_k_lists([None]) is None
    assert list_to_python(merge_k_lists([build_list([1])])) == [1]
    print("All tests passed!")
