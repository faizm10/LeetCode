"""
p32. Alien Dictionary (Hard)
Topic: Topological Sort
Known as a frequently-asked Google interview question.

You're given a list of words sorted lexicographically according to an
unknown alien alphabet. Derive a valid ordering of the letters used.
Multiple valid orderings may exist -- return any one of them, as a string
containing each distinct letter exactly once.

Contract: if no valid ordering exists (the constraints form a cycle, or a
word is an invalid prefix -- e.g. a longer word appears before its own
prefix), return "" (empty string).

Example:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: any string consistent with: w before e, r before t, t before f
        (e.g. "wertf" is one valid answer, but not the only one)
"""

from collections import defaultdict, deque


def alien_order(words):
    adj = defaultdict(set)
    in_degree = {c: 0 for w in words for c in w}

    for w1, w2 in zip(words, words[1:]):
        min_len = min(len(w1), len(w2))
        divergent = False
        for i in range(min_len):
            if w1[i] != w2[i]:
                if w2[i] not in adj[w1[i]]:
                    adj[w1[i]].add(w2[i])
                    in_degree[w2[i]] += 1
                divergent = True
                break
        if not divergent and len(w1) > len(w2):
            return ""

    queue = deque(c for c in in_degree if in_degree[c] == 0)
    order = []
    while queue:
        c = queue.popleft()
        order.append(c)
        for nxt in adj[c]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(order) != len(in_degree):
        return ""  # cycle
    return "".join(order)


def _build_constraints(words):
    constraints = set()
    for w1, w2 in zip(words, words[1:]):
        min_len = min(len(w1), len(w2))
        found_diff = False
        for i in range(min_len):
            if w1[i] != w2[i]:
                constraints.add((w1[i], w2[i]))
                found_diff = True
                break
        if not found_diff and len(w1) > len(w2):
            return None
    return constraints


def _check_order(order, words):
    constraints = _build_constraints(words)
    if constraints is None:
        return order == ""
    if order == "":
        return False
    letters = set("".join(words))
    if set(order) != letters or len(order) != len(letters):
        return False
    pos = {c: i for i, c in enumerate(order)}
    return all(pos[a] < pos[b] for a, b in constraints)


if __name__ == "__main__":
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    assert _check_order(alien_order(words1), words1)

    words2 = ["z", "x"]
    assert _check_order(alien_order(words2), words2)

    words3 = ["z", "x", "z"]  # cycle: z<x and x<z -- impossible
    assert alien_order(words3) == ""

    words4 = ["abc", "ab"]  # invalid prefix order
    assert alien_order(words4) == ""

    words5 = ["abc"]
    result5 = alien_order(words5)
    assert set(result5) == {"a", "b", "c"} and len(result5) == 3

    print("All tests passed!")
