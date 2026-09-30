"""
p02. Valid Anagram (Easy)
Topic: Arrays / Hashing

Given two strings s and t, return True if t is an anagram of s (uses
exactly the same letters with the same multiplicities), and False otherwise.

Example:
Input: s = "anagram", t = "nagaram"
Output: True
"""


def is_anagram(s, t):
    if len(s) != len(t): #if the length isnt the same, we can return false
        return False
    return sorted(s) == sorted(t) # if the sorted strings are equal, then they are anagrams of each other


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    assert is_anagram("aacc", "ccac") is False
    print("All tests passed!")
