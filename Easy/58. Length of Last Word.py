class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lol = s.split(" ")
        lol = [word for word in lol if word != ""]
        return len(lol[-1])
        