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
        self.stack = []  # each entry: (value, min_so_far)

    def push(self, val):
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def get_min(self):
        return self.stack[-1][1]


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
