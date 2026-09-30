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
    def __init__(self, num_buckets=1000):
        self.num_buckets = num_buckets
        self.buckets = [[] for _ in range(num_buckets)]

    def _bucket(self, key):
        return self.buckets[key % self.num_buckets]

    def put(self, key, value):
        bucket = self._bucket(key)
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        bucket = self._bucket(key)
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key):
        bucket = self._bucket(key)
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return


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
