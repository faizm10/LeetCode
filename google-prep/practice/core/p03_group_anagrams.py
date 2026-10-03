"""
p03. Group Anagrams (Medium)
Topic: Arrays / Hashing

Given an array of strings, group the anagrams together. You can return the
groups in any order, and the strings within a group in any order.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
"""


from numpy import sort


def group_anagrams(strs):
    # we need to sort the strings in a way where if 2 or more strings are anagrams, we put it in group 1.
    groups = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in groups:
            groups[sorted_s] = []
        groups[sorted_s].append(s)

    return list(groups.values())

def _normalize(groups):
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    assert _normalize(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == _normalize(
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    )
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    print("All tests passed!")
