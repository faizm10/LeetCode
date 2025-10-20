class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {} # we want to capture the dict of the s1
        m = len(s1)
        n = len(s2)
        if s1 > s2: #if s1 is > s2: return false due to length
            return False
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        win = {} #set current window to see if it matches need
        for ch in s2[:m]: # we loop to the length of the s1 to see what does the current window have
            win[ch] = win.get(ch, 0) + 1
        if win == need: return True
        for i in range(m, n):               # slide the window one step at a time, starting right after the first window
            add = s2[i]                     # the new character entering on the RIGHT
            rem = s2[i - m]                 # the old character leaving from the LEFT

            win[add] = win.get(add, 0) + 1  # include the new right char in the window count

            win[rem] -= 1                   # remove the left char from the window count (it slid out)
            if win[rem] == 0:               # if its count is now zero...
                del win[rem]                # ...delete the key to keep dicts clean (so win == need works)

            if win == need:                 # if the current window’s counts match s1’s counts,
                return True                 # ...we found a permutation

        return False