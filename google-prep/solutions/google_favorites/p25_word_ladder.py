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
    words = set(word_list)
    if end_word not in words:
        return 0

    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return steps
        for i in range(len(word)):
            for ch in string.ascii_lowercase:
                if ch == word[i]:
                    continue
                candidate = word[:i] + ch + word[i + 1 :]
                if candidate in words and candidate not in visited:
                    visited.add(candidate)
                    queue.append((candidate, steps + 1))

    return 0


if __name__ == "__main__":
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert ladder_length("a", "c", ["a", "b", "c"]) == 2
    assert ladder_length("hot", "dog", ["hot", "dog"]) == 0
    print("All tests passed!")
