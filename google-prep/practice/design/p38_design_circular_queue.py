"""
p38. Design Circular Queue (Medium)
Topic: Design / Arrays

Design a fixed-size circular queue backed by an array (not a list that
grows/shrinks with insert(0)/pop(0) -- use two pointers and a fixed-size
array so all operations are O(1)). Implement:
  en_queue(value) -> True if inserted, False if the queue was full
  de_queue()      -> True if removed, False if the queue was empty
  front()          -> front element, or -1 if empty
  rear()           -> rear element, or -1 if empty
  is_empty()       -> bool
  is_full()        -> bool

Example:
q = MyCircularQueue(3)
q.en_queue(1)  -> True
q.en_queue(2)  -> True
q.en_queue(3)  -> True
q.en_queue(4)  -> False   (full)
q.rear()       -> 3
q.is_full()    -> True
q.de_queue()   -> True
q.en_queue(4)  -> True
q.rear()       -> 4
"""


class MyCircularQueue:
    def __init__(self, k):
        # TODO: implement
        pass

    def en_queue(self, value):
        # TODO: implement
        pass

    def de_queue(self):
        # TODO: implement
        pass

    def front(self):
        # TODO: implement
        pass

    def rear(self):
        # TODO: implement
        pass

    def is_empty(self):
        # TODO: implement
        pass

    def is_full(self):
        # TODO: implement
        pass


if __name__ == "__main__":
    q = MyCircularQueue(3)
    assert q.is_empty() is True
    assert q.en_queue(1) is True
    assert q.en_queue(2) is True
    assert q.en_queue(3) is True
    assert q.en_queue(4) is False
    assert q.rear() == 3
    assert q.is_full() is True
    assert q.de_queue() is True
    assert q.en_queue(4) is True
    assert q.rear() == 4
    assert q.front() == 2

    q2 = MyCircularQueue(1)
    assert q2.en_queue(10) is True
    assert q2.is_full() is True
    assert q2.front() == 10
    assert q2.rear() == 10
    assert q2.de_queue() is True
    assert q2.is_empty() is True
    assert q2.de_queue() is False
    assert q2.front() == -1
    print("All tests passed!")
