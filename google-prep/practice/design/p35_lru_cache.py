"""
p35. LRU Cache (Medium)
Topic: Design

Design a Least Recently Used (LRU) cache with fixed capacity. Implement:
  get(key)         -> return the value, or -1 if not present. Marks the
                       key as most recently used.
  put(key, value)   -> insert/update the value. If this exceeds capacity,
                       evict the least recently used key first.
Both operations must run in O(1) average time.

Example:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)      -> 1
cache.put(3, 3)   -> evicts key 2 (least recently used)
cache.get(2)      -> -1
"""


class LRUCache:
    def __init__(self, capacity):
        # TODO: implement
        pass

    def get(self, key):
        # TODO: implement
        pass

    def put(self, key, value):
        # TODO: implement
        pass


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache2 = LRUCache(1)
    cache2.put(1, 1)
    assert cache2.get(1) == 1
    cache2.put(2, 2)  # evicts key 1
    assert cache2.get(1) == -1
    assert cache2.get(2) == 2
    print("All tests passed!")
