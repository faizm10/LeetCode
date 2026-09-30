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


def character_replacement(s, k):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("", 0) == 0
    assert character_replacement("AAAA", 0) == 4
    print("All tests passed!")
