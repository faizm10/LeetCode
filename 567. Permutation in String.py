class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        m = len(s1)
        n = len(s2)
        if s1 > s2: 
            return False
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        win = {} #set current window to see if it matches need
        for ch in s2[:m]:
            win[ch] = win.get(ch, 0) + 1
        if win == need: return True

        for i in range(m, n):
            add = s2[i]
            rem = s2[i - m]
            win[add] = win.get(add, 0) + 1
            win[rem] -= 1                      # shrink
            if win[rem] == 0:
                del win[rem]
            if win == need: return True
        return False