"""
p29. Moving Average from Data Stream (Easy)
Topic: Queues / Design
Known as a frequently-asked Google interview question.

Given a window size, implement a data structure that calculates the moving
average of the last `size` values in a stream of integers each time a new
value arrives (using fewer than `size` values while the stream is still
filling up).

Example:
m = MovingAverage(3)
m.next(1)  -> 1.0            (window: [1])
m.next(10) -> 5.5            (window: [1,10])
m.next(3)  -> 4.666...       (window: [1,10,3])
m.next(5)  -> 6.0            (window: [10,3,5], 1 fell out)
"""

from collections import deque


class MovingAverage:
    def __init__(self, size):
        # TODO: implement
        pass

    def next(self, val):
        # TODO: implement
        pass


if __name__ == "__main__":
    m = MovingAverage(3)
    assert m.next(1) == 1.0
    assert m.next(10) == 5.5
    assert abs(m.next(3) - 14 / 3) < 1e-9
    assert abs(m.next(5) - 6.0) < 1e-9

    m2 = MovingAverage(1)
    assert m2.next(7) == 7.0
    assert m2.next(2) == 2.0
    print("All tests passed!")
