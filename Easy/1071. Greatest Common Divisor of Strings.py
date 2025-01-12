import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        d = math.gcd(len(str1), len(str2))
        if (str1[:d] == str2[:d]):
            return str1[:d]
        else:
            return ""