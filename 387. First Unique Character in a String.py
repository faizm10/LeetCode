class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1: # index 1 = 1
                return i # return the value of that index aka counting

        return -1