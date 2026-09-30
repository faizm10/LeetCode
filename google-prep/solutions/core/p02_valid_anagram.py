"""
p02. Valid Anagram (Easy)
Topic: Arrays / Hashing

Given two strings s and t, return True if t is an anagram of s (uses
exactly the same letters with the same multiplicities), and False otherwise.

Example:
Input: s = "anagram", t = "nagaram"
Output: True
"""

from collections import Counter


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    assert is_anagram("aacc", "ccac") is False
    print("All tests passed!")
