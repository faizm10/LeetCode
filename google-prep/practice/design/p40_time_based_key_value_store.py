"""
p40. Time Based Key-Value Store (Medium)
Topic: Design / Binary Search

Design a time-based key-value store. Implement:
  set(key, value, timestamp) -> stores the key with this value at this
                                 timestamp (timestamps are strictly
                                 increasing per key across calls)
  get(key, timestamp)        -> returns the value associated with the key
                                 at the largest recorded timestamp that is
                                 <= the given timestamp; "" if none exists

Example:
store = TimeMap()
store.set("foo", "bar", 1)
store.get("foo", 1)   -> "bar"
store.get("foo", 3)   -> "bar"   (no entry at ts=3, most recent <=3 is ts=1)
store.set("foo", "bar2", 4)
store.get("foo", 4)   -> "bar2"
store.get("foo", 5)   -> "bar2"
store.get("foo", 0)   -> ""      (nothing recorded yet at ts<=0)
"""

import bisect


class TimeMap:
    def __init__(self):
        # TODO: implement
        pass

    def set(self, key, value, timestamp):
        # TODO: implement
        pass

    def get(self, key, timestamp):
        # TODO: implement
        pass


if __name__ == "__main__":
    store = TimeMap()
    store.set("foo", "bar", 1)
    assert store.get("foo", 1) == "bar"
    assert store.get("foo", 3) == "bar"
    store.set("foo", "bar2", 4)
    assert store.get("foo", 4) == "bar2"
    assert store.get("foo", 5) == "bar2"
    assert store.get("foo", 0) == ""
    assert store.get("missing_key", 1) == ""
    print("All tests passed!")
