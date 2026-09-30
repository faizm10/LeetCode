"""
p10. Longest Substring Without Repeating Characters (Medium)
Topic: Sliding Window

Given a string s, find the length of the longest substring without
repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3   ("abc")
"""


def length_of_longest_substring(s):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    print("All tests passed!")
