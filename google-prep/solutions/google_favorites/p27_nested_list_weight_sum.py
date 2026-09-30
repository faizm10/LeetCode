"""
p27. Nested List Weight Sum (Medium)
Topic: Recursion / DFS
Known as a frequently-asked Google interview question.

Adapted from LeetCode's NestedInteger-interface version: here the input is
just a plain Python nested list of ints, e.g. [1, [4, [6]]], where an
element is either an int or another (possibly nested) list. Return the sum
of every integer multiplied by its depth (the outermost list is depth 1).

Example:
Input: nested_list = [[1,1],2,[1,1]]
Output: 10   (four 1's at depth 2 = 8, one 2 at depth 1 = 2, total 10)

Input: nested_list = [1,[4,[6]]]
Output: 27   (1*1 + 4*2 + 6*3 = 1 + 8 + 18 = 27)
"""


def depth_sum(nested_list):
    def helper(items, depth):
        total = 0
        for item in items:
            if isinstance(item, list):
                total += helper(item, depth + 1)
            else:
                total += item * depth
        return total

    return helper(nested_list, 1)


if __name__ == "__main__":
    assert depth_sum([[1, 1], 2, [1, 1]]) == 10
    assert depth_sum([1, [4, [6]]]) == 27
    assert depth_sum([]) == 0
    assert depth_sum([5]) == 5
    assert depth_sum([[[5]]]) == 15
    print("All tests passed!")
