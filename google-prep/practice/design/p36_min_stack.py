"""
p36. Min Stack (Medium)
Topic: Design

Design a stack that supports push, pop, top, and retrieving the minimum
element, all in O(1) time.

Example:
s = MinStack()
s.push(-2); s.push(0); s.push(-3)
s.get_min()  -> -3
s.pop()
s.top()      -> 0
s.get_min()  -> -2
"""


class MinStack:
    def __init__(self):
        # TODO: implement
        pass

    def push(self, val):
        # TODO: implement
        pass

    def pop(self):
        # TODO: implement
        pass

    def top(self):
        # TODO: implement
        pass

    def get_min(self):
        # TODO: implement
        pass


if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.get_min() == -3
    s.pop()
    assert s.top() == 0
    assert s.get_min() == -2

    s2 = MinStack()
    s2.push(5)
    s2.push(5)
    s2.push(2)
    assert s2.get_min() == 2
    s2.pop()
    assert s2.get_min() == 5
    print("All tests passed!")
