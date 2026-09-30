"""
p37. Design HashMap (Easy)
Topic: Design

Implement a HashMap without using Python's built-in dict/set for storage.
Support:
  put(key, value) -> insert or update
  get(key)        -> return the value, or -1 if the key doesn't exist
  remove(key)      -> remove the mapping if it exists

Use an array of fixed-size buckets with chaining (each bucket a list of
[key, value] pairs) to handle collisions via hashing (key % num_buckets).

Example:
m = MyHashMap()
m.put(1, 1)
m.put(2, 2)
m.get(1)     -> 1
m.get(3)     -> -1
m.put(2, 1)  -> updates
m.get(2)     -> 1
m.remove(2)
m.get(2)     -> -1
"""


class MyHashMap:
    def __init__(self):
        # TODO: implement (e.g. self.buckets = [[] for _ in range(N)])
        pass

    def put(self, key, value):
        # TODO: implement
        pass

    def get(self, key):
        # TODO: implement
        pass

    def remove(self, key):
        # TODO: implement
        pass


if __name__ == "__main__":
    m = MyHashMap()
    m.put(1, 1)
    m.put(2, 2)
    assert m.get(1) == 1
    assert m.get(3) == -1
    m.put(2, 1)
    assert m.get(2) == 1
    m.remove(2)
    assert m.get(2) == -1
    m.remove(999)  # removing a missing key should not error

    # exercise collisions: with any reasonable bucket count, some of these
    # keys should land in the same bucket
    for k in range(50):
        m.put(k, k * 10)
    for k in range(50):
        assert m.get(k) == k * 10
    m.remove(25)
    assert m.get(25) == -1
    assert m.get(24) == 240
    print("All tests passed!")
