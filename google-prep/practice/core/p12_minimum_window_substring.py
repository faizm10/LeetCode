"""
p12. Minimum Window Substring (Hard)
Topic: Sliding Window

Given strings s and t, return the minimal substring of s such that every
character in t (including duplicates) is included in the substring. If no
such substring exists, return "".

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""


def min_window(s, t):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("", "a") == ""
    assert min_window("ab", "b") == "b"
    print("All tests passed!")
