class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        seen = set() #want to find unique for substring
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            best=max(best,r-l+1)
        return best
    
    ##feb 12

 class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, count = 0, 0 ,0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            count = max(count,r-l+1)
        return count
                   