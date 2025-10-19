class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #intuituon:
        freq = {}
        best = 0
        left = 0
        right = 0
        window = 0
        for right, ch in enumerate(s): #tracks the index and value
            freq[ch] = freq.get(ch, 0) + 1 
            if (window - freq[ch] <=k):
                window+=1
        return window
# https://stackoverflow.com/questions/8703496/hash-map-in-python