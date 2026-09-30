# Google OA / Interview Prep — Offline Practice Set

Fully offline. Python 3 stdlib only — no internet, no judge, no pip installs
needed. Everything runs with a plain `python3 file.py`.

## How to use

1. Open a file under `practice/<category>/pXX_*.py`.
2. Read the docstring at the top — problem statement, constraints, example.
3. Implement the function/class where you see `# TODO: implement`.
4. Run it: `python3 practice/<category>/pXX_*.py`
   The `if __name__ == "__main__":` block at the bottom is your local judge
   — a set of `assert`s. No output/no error = you didn't finish; a stack
   trace on an `assert` = close but wrong; `All tests passed!` = correct.
5. Stuck, or want to compare after solving it? The matching file under
   `solutions/<category>/pXX_*.py` has a working reference implementation
   with the identical problem statement and tests.

## Layout

- `practice/core/` (p01–p24) — arrays/hashing, two pointers, sliding
  window, binary search, intervals, linked lists, trees, graphs. The bread
  and butter of Google's OA and phone screens.
- `practice/google_favorites/` (p25–p34) — problems that circulate
  specifically as frequently-asked at Google (Word Ladder, Meeting Rooms
  II, Alien Dictionary, Merge K Sorted Lists, etc.).
- `practice/design/` (p35–p40) — LRU Cache, Min Stack, and other
  "design a data structure" problems, a different mode of thinking than
  pure algorithms (API design, encapsulation, edge cases on state).

`solutions/` mirrors the same structure.

## Suggested pacing for a 14-hour flight

- **Hour 1** — warm-up on 2–3 easy `core/` problems (p01, p02, p18) to get
  your fingers moving without pressure.
- **Hours 2–6** — work through `core/` topic by topic in order. Don't skip
  around; the ordering roughly follows a difficulty/topic progression.
- **Hours 7–9** — `google_favorites/` as a change of pace mid-flight —
  these lean more on recognizing a pattern (BFS shortest path, heap merge,
  topological sort) than raw implementation grind.
- **Hours 10–11** — `design/` problems last — switch mental gears from
  "solve an algorithm" to "design a clean API with the right state."
- **Remaining time** — review. Re-attempt anything you had to peek at the
  solution for, from scratch, without looking.

40 problems at ~20 min average is the full set — but it's fine, expected
even, to not finish all 40. Solving 20 well with a genuine review pass
beats rushing all 40. If a problem takes more than ~25–30 minutes without
progress, peek at the solution's approach (not the code), then re-implement
it yourself — that's a better use of a fixed block of flight time than
grinding in silence.

## Note on this repo's automation

This repo has a git hook (`.githooks/post-commit`) that auto-opens/merges
a PR for any committed file named like `42. Trapping Rain Water.py`. Files
in this folder deliberately use a different naming scheme (`pXX_snake_case.py`)
so committing `google-prep/` won't trigger that automation. Committing it
is your call, whenever you want — not done automatically.
