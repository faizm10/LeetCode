"""
p11. Longest Repeating Character Replacement (Medium)
Topic: Sliding Window

Given a string s and an integer k, you can change up to k characters in s
to any other uppercase letter. Return the length of the longest substring
containing the same letter after performing at most k replacements.

Example:
Input: s = "ABAB", k = 2
Output: 4
"""

from collections import defaultdict


def character_replacement(s, k):
    counts = defaultdict(int)
    start = 0
    max_freq = 0
    best = 0
    for end, c in enumerate(s):
        counts[c] += 1
        max_freq = max(max_freq, counts[c])
        window_len = end - start + 1
        if window_len - max_freq > k:
            counts[s[start]] -= 1
            start += 1
        else:
            best = max(best, window_len)
    return best


if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("", 0) == 0
    assert character_replacement("AAAA", 0) == 4
    print("All tests passed!")
