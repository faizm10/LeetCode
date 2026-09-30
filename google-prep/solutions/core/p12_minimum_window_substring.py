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

from collections import Counter


def min_window(s, t):
    if not s or not t:
        return ""

    need = Counter(t)
    missing = len(t)
    best_len = float("inf")
    best_start = 0
    start = 0

    for end, c in enumerate(s):
        if need[c] > 0:
            missing -= 1
        need[c] -= 1

        while missing == 0:
            if end - start + 1 < best_len:
                best_len = end - start + 1
                best_start = start
            need[s[start]] += 1
            if need[s[start]] > 0:
                missing += 1
            start += 1

    return "" if best_len == float("inf") else s[best_start : best_start + best_len]


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("", "a") == ""
    assert min_window("ab", "b") == "b"
    print("All tests passed!")
