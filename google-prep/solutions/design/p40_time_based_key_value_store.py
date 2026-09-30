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
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> list of (timestamp, value), sorted by timestamp

    def set(self, key, value, timestamp):
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        entries = self.store.get(key)
        if not entries:
            return ""
        i = bisect.bisect_right(entries, (timestamp, chr(0x10FFFF)))
        if i == 0:
            return ""
        return entries[i - 1][1]


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
