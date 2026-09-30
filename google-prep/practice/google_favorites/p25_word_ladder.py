"""
p25. Word Ladder (Hard)
Topic: BFS / Graphs
Known as a frequently-asked Google interview question.

Given begin_word, end_word, and a word_list, return the number of words in
the shortest transformation sequence from begin_word to end_word, where
each step changes exactly one letter and each intermediate word must exist
in word_list. Return 0 if no such sequence exists. end_word must be in
word_list to be reachable; begin_word does not need to be.

Example:
Input: begin_word = "hit", end_word = "cog",
       word_list = ["hot","dot","dog","lot","log","cog"]
Output: 5   ("hit" -> "hot" -> "dot" -> "dog" -> "cog")
"""

from collections import deque
import string


def ladder_length(begin_word, end_word, word_list):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert ladder_length("a", "c", ["a", "b", "c"]) == 2
    assert ladder_length("hot", "dog", ["hot", "dog"]) == 0
    print("All tests passed!")
