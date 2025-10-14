class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_letters = "".join(ch for ch in s if ch.isalpha())
        return only_letters.lower() == only_letters.lower()[::-1]

