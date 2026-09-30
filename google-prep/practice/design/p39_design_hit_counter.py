"""
p39. Design Hit Counter (Medium)
Topic: Design / Queues

Design a hit counter that counts hits received in the past 300 seconds
(5 minutes), a rolling window. Calls to hit(timestamp) arrive with
timestamps in non-decreasing order (seconds granularity).
  hit(timestamp)       -> record a hit at this timestamp
  get_hits(timestamp)  -> return the number of hits in
                           (timestamp - 300, timestamp], inclusive of
                           timestamp itself

Example:
c = HitCounter()
c.hit(1)
c.hit(2)
c.hit(3)
c.get_hits(4)    -> 3
c.hit(300)
c.get_hits(300)  -> 4
c.get_hits(301)  -> 3   (the hit at timestamp 1 has aged out)
"""

from collections import deque


class HitCounter:
    def __init__(self):
        # TODO: implement
        pass

    def hit(self, timestamp):
        # TODO: implement
        pass

    def get_hits(self, timestamp):
        # TODO: implement
        pass


if __name__ == "__main__":
    c = HitCounter()
    c.hit(1)
    c.hit(2)
    c.hit(3)
    assert c.get_hits(4) == 3
    c.hit(300)
    assert c.get_hits(300) == 4
    assert c.get_hits(301) == 3
    assert c.get_hits(600) == 0  # everything has aged out of the 300s window
    assert c.get_hits(601) == 0
    print("All tests passed!")
