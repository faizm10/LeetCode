class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_letters = "".join(ch for ch in s if ch.isalpha())
        print(only_letters.lower())
        i,j = 0, len(only_letters)-1
        while i < j:
            if only_letters[i] != only_letters[j]:
                return False
            i +=1
            j -=1
        return True


