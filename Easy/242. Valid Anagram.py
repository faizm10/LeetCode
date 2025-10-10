class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #could compare first and last index, while decresing
        s = sorted(s)
        t = sorted(t)
        return s == t
    
        # another optimal solution with 17ms:
        #return sorted(s) == sorted(t)