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
    left = 0
    best = 0
    current = 0
    duplicate = set()
    for right in range(len(s)):
            # right = 0, 
            
        if s[right] not in duplicate:
            duplicate.add(s[right])
            current+=1
        else:
            best = max(best,current)
            duplicate.discard(s[left])
            duplicate.add(s[right])
            left+=1
            
    return best


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    print("All tests passed!")
