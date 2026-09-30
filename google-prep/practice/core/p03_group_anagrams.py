"""
p03. Group Anagrams (Medium)
Topic: Arrays / Hashing

Given an array of strings, group the anagrams together. You can return the
groups in any order, and the strings within a group in any order.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
"""


def group_anagrams(strs):
    # TODO: implement
    pass


def _normalize(groups):
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    assert _normalize(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == _normalize(
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    )
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    print("All tests passed!")
