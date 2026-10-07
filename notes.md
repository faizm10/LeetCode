# leetcode notes

## table of contents

1. [big o](#big-o)
2. [arrays](#arrays)
3. [strings](#strings)
4. [hashmaps (dictionaries)](#hashmaps-dictionaries)
5. [sets](#sets)
6. [two pointers](#two-pointers)
7. [sliding window](#sliding-window)
8. [prefix sums](#prefix-sums)
9. [stacks](#stacks)
10. [queues](#queues)
11. [binary search](#binary-search)
12. [sorting](#sorting)
13. [linked lists](#linked-lists)
14. [recursion](#recursion)
15. [trees](#trees)
16. [heaps](#heaps)
17. [intervals](#intervals)
18. [greedy](#greedy)
19. [backtracking](#backtracking)
20. [graphs](#graphs)
21. [dynamic programming](#dynamic-programming)
22. [tries](#tries)
23. [which pattern to use](#which-pattern-to-use)

## big o

big o tells you how the time (or memory) your code needs **grows** as the input gets bigger. `n` is the size of the input.

| big o | name | example |
|---|---|---|
| O(1) | constant | `nums[0]`, dict lookup |
| O(log n) | logarithmic | binary search (cut in half each step) |
| O(n) | linear | one loop over the array |
| O(n log n) | n log n | sorting |
| O(n²) | quadratic | loop inside a loop |
| O(2ⁿ) | exponential | trying every subset |

fastest at the top, slowest at the bottom.

### quick rules
- one loop → O(n)
- loop inside a loop → O(n²)
- cutting the problem in half each step → O(log n)
- sorting → O(n log n)
- drop constants: O(2n) is just O(n)
- keep the biggest term: O(n² + n) is just O(n²)

### space
space complexity is the extra memory you use. making a new list or dict of size n → O(n) space. a few variables → O(1) space.

### rough limits (what will run in time)
| n up to | aim for |
|---|---|
| 10 to 20 | O(2ⁿ) is fine |
| 1,000 | O(n²) is fine |
| 100,000+ | need O(n) or O(n log n) |

## arrays

list of items stored in order. you access items by index.

### create an array
```python
array = [1, 2, 3]
```

### access an item
```python
print(array[2])  # 3
```

### add item
```python
array.append(6)  # [1, 2, 3, 6]
```

### remove item
```python
del array[0]
```

### update item
```python
array[1] = 10
```

### iterate
```python
for item in array:
    print(item)
```

### find length
```python
len(array)
```

## strings

sequence of characters stored in order. works a lot like an array (index, slice, loop), but strings are **immutable**: you can't change a character in place, every change makes a new string.

### create a string
```python
s = "hello"
```

### access a character
```python
s[0]   # 'h'
s[-1]  # 'o' (negative index counts from the end)
```

### slicing
```python
s[1:4]   # 'ell' (start included, end excluded)
s[:2]    # 'he'
s[2:]    # 'llo'
s[::-1]  # 'olleh' (reverse a string)
```

### update a character
```python
s[0] = 'j'          # error, strings are immutable
s = 'j' + s[1:]     # 'jello', make a new string instead
```

### iterate
```python
for char in s:
    print(char)

for i, char in enumerate(s):  # index + character
    print(i, char)
```

### find length
```python
len(s)  # 5
```

### change case
```python
s.upper()  # 'HELLO'
s.lower()  # 'hello'
```

### check character type
```python
'a'.isalpha()  # True, letter
'5'.isdigit()  # True, number
'a'.isalnum()  # True, letter or number (good for skipping punctuation)
' '.isspace()  # True, whitespace
```

### split and join
```python
"a b c".split()     # ['a', 'b', 'c'] (splits on whitespace)
"a,b,c".split(",")  # ['a', 'b', 'c']
"-".join(['a', 'b', 'c'])  # 'a-b-c'
```

### strip whitespace
```python
"  hi  ".strip()  # 'hi'
```

### find and replace
```python
"hello".find("l")         # 2 (first index, -1 if not found)
"hello".count("l")        # 2
"hello".replace("l", "L") # 'heLLo'
"ell" in "hello"          # True
```

### convert between string and list
```python
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']
"".join(chars)         # 'hello'
```

### characters to numbers
```python
ord('a')  # 97
chr(97)   # 'a'
ord('c') - ord('a')  # 2 (position in the alphabet, useful for arrays of size 26)
```

### count characters
```python
from collections import Counter
Counter("hello")  # {'l': 2, 'h': 1, 'e': 1, 'o': 1}
```

### common pattern (build a string efficiently)
```python
# adding to a string in a loop makes a new string every time (slow)
# add to a list, then join once at the end
result = []
for char in s:
    result.append(char.upper())
"".join(result)  # 'HELLO'
```

### common pattern (check palindrome)
```python
s == s[::-1]
```

## hashmaps (dictionaries)

a hashmap stores **key → value** pairs. in python it's called a `dict`.

it runs each key through a hash function ("secret formula") that turns the key into a spot in memory. so instead of searching through every item, it jumps straight to the right spot. that's why lookups are fast.

> **the big idea:** a hashmap trades memory for speed. you spend O(n) space to turn an O(n) search into an O(1) lookup. most "make this faster than O(n²)" problems are solved this way.

### how fast is it?

| operation | time |
|---|---|
| look up a key | O(1) |
| add / update a key | O(1) |
| delete a key | O(1) |
| check `key in d` | O(1) |
| loop over everything | O(n) |

O(1) here is on average. it's almost always true in practice, so treat it as O(1) in interviews.

### basics

```python
d = {"apple": 1, "banana": 2}   # create
d = {}                          # empty dict

d["cherry"] = 3       # add
d["apple"] = 10       # update (same syntax as add)
d["banana"]           # access → 2
del d["apple"]        # remove (error if the key isn't there)
d.pop("banana")       # remove and give back the value → 2
d.pop("zzz", None)    # remove, no error if missing

len(d)                # number of keys
"cherry" in d         # True (checks keys, not values)
```

### looping

```python
for key in d:                  # keys
for value in d.values():       # values
for key, value in d.items():   # both (use this most)
```

since python 3.7, dicts remember the order you added keys in.

### safe lookups (no KeyError)

`d["missing"]` crashes with a `KeyError`. use these instead:

```python
d.get("missing")        # None
d.get("missing", 0)     # 0 (your default)

# count something without checking first
count[x] = count.get(x, 0) + 1
```

### defaultdict (auto-creates missing keys)

```python
from collections import defaultdict

count = defaultdict(int)     # missing keys start at 0
count["a"] += 1              # no need to check first

groups = defaultdict(list)   # missing keys start as []
groups["fruit"].append("apple")
```

use `int` for counting, `list` for grouping, `set` for grouping without duplicates.

### Counter (counts things for you)

```python
from collections import Counter

c = Counter("banana")     # {'a': 3, 'n': 2, 'b': 1}
c["a"]                    # 3
c["z"]                    # 0 (missing keys give 0, no error)
c.most_common(2)          # [('a', 3), ('n', 2)]

Counter("listen") == Counter("silent")  # True, same letters
```

### what can be a key?

keys must be **immutable** (they can't change).

| ✅ allowed | ❌ not allowed |
|---|---|
| `int`, `str`, `float`, `bool` | `list` |
| `tuple` (if everything inside is immutable) | `dict` |
| `frozenset` | `set` |

need a list as a key? turn it into a tuple first: `d[tuple(my_list)] = ...`

### sorting a dict

```python
sorted(d)                                    # keys, sorted
sorted(d.items(), key=lambda kv: kv[1])      # pairs, by value (smallest first)
sorted(d.items(), key=lambda kv: -kv[1])     # pairs, by value (biggest first)
max(d, key=d.get)                            # key with the biggest value
```

### common pattern (two sum: "have I seen what I need?")

store each number's index as you go. for every new number, check if its partner is already in the map.

```python
def two_sum(nums, target):
    seen = {}                        # number → index
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
```

O(n) instead of O(n²) for two loops.

### common pattern (count frequencies)

```python
count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1

# or just: count = Counter(nums)
```

used in: valid anagram, first unique character, majority element.

### common pattern (group by a key)

pick something that's the **same for every item in a group**, and use it as the key.

```python
# group anagrams: "eat", "tea", "ate" all sort to "aet"
groups = defaultdict(list)
for word in words:
    key = "".join(sorted(word))     # or tuple of 26 letter counts
    groups[key].append(word)
return list(groups.values())
```

### common pattern (top k frequent, bucket sort)

```python
count = Counter(nums)
buckets = [[] for _ in range(len(nums) + 1)]   # index = frequency
for num, freq in count.items():
    buckets[freq].append(num)

result = []
for freq in range(len(buckets) - 1, 0, -1):    # highest frequency first
    for num in buckets[freq]:
        result.append(num)
        if len(result) == k:
            return result
```

O(n). the easier version is `[x for x, _ in Counter(nums).most_common(k)]`, which is O(n log n).

### common pattern (prefix sum + hashmap)

count subarrays that add up to `k`. see [prefix sums](#prefix-sums) for the full version. the trick is storing **how many times** each running sum has appeared:

```python
seen = {0: 1}     # running sum → how many times we've seen it
```

### common mistakes

- reading a missing key with `d[key]` → use `d.get(key, default)` or `defaultdict`
- changing a dict while looping over it → loop over `list(d)` instead
- using a list as a key → convert it to a `tuple`
- `{}` is an empty **dict**, not an empty set → use `set()`
- `x in d` checks keys only → use `x in d.values()` for values (that one is O(n))

### hashmap vs set

| use a... | when you need |
|---|---|
| set | "have I seen this?" (yes / no) |
| hashmap | "have I seen this, **and** what do I know about it?" (index, count, list...) |

## sets

`set()` is a collection of unique items. stores multiple items in a single variable and removes any duplicates.

- useful if we want to see unique numbers
- useful to check if an item exists in a collection

### create a set
```python
my_set = {1, 2, 3}
empty_set = set()  # {} makes a dict, not a set
```

### remove duplicates from a list
```python
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)  # {1, 2, 3}
```

### add item
```python
my_set.add(4)  # {1, 2, 3, 4}
my_set.add(2)  # already there, nothing changes
```

### remove item
```python
my_set.remove(4)   # error if 4 isn't in the set
my_set.discard(9)  # no error if 9 isn't in the set
```

### check if item exists
```python
if 2 in my_set:  # fast lookup, like a dictionary
    print("found")
```

### find length
```python
len(my_set)  # 3
```

### iterate
```python
# sets have no order, so the output order isn't guaranteed
for item in my_set:
    print(item)
```

### common pattern (check for duplicates)
```python
seen = set()
for num in nums:
    if num in seen:
        return True
    seen.add(num)
return False
```

## two pointers

use two indexes that move toward each other (or in the same direction). works great on **sorted** arrays.

### template (pair that sums to target)
```python
left = 0
right = len(nums) - 1
while left < right:
    total = nums[left] + nums[right]

    if total == target:
        return True
    elif total < target:
        left += 1
    else:
        right -= 1
return False
```

### when to use
- the array is **sorted** and you're looking for a pair
- comparing things from both ends (palindromes, container with most water)
- moving or removing items in place

### template (same direction, remove duplicates in place)
```python
# slow marks where the next unique item goes, fast scans ahead
slow = 1
for fast in range(1, len(nums)):
    if nums[fast] != nums[fast - 1]:
        nums[slow] = nums[fast]
        slow += 1
return slow  # number of unique items
```

### common pattern (check palindrome, skipping punctuation)
```python
left, right = 0, len(s) - 1
while left < right:
    if not s[left].isalnum():
        left += 1
    elif not s[right].isalnum():
        right -= 1
    elif s[left].lower() != s[right].lower():
        return False
    else:
        left += 1
        right -= 1
return True
```

time: O(n). space: O(1).

## sliding window

we use it when we care about a **continuous section** of an array or string.

- **fixed-size window**: window stays the same size.
  - example: "maximum sum of 3 consecutive numbers"
- **variable-size window**:
  - right → expands the window
  - left → shrinks the window when needed
  - example: "longest substring without duplicates"

### template
```python
left = 0

for right in range(len(nums)):
    # expand window

    while window_is_bad:
        # shrink window
        left += 1

    # update answer
```

### fixed-size window (max sum of k numbers in a row)
```python
window_sum = sum(nums[:k])
best = window_sum
for right in range(k, len(nums)):
    window_sum += nums[right] - nums[right - k]  # add new, remove old
    best = max(best, window_sum)
return best
```

### common pattern (longest substring without repeating characters)
```python
seen = set()
left = 0
best = 0
for right in range(len(s)):
    while s[right] in seen:      # window is bad, shrink it
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    best = max(best, right - left + 1)
return best
```

### counting characters in the window
```python
count = {}
count[s[right]] = count.get(s[right], 0) + 1  # add on the right
count[s[left]] -= 1                           # remove on the left
left += 1
max(count.values())  # how many times the most common letter appears
```

window size is always `right - left + 1`.

time: O(n), since each item enters and leaves the window once.

## prefix sums

save a running total so you can get the sum of **any range** in O(1) instead of looping every time.

### build it
```python
nums = [2, 4, 1, 3]
prefix = [0]
for num in nums:
    prefix.append(prefix[-1] + num)
# prefix = [0, 2, 6, 7, 10]
```

### sum of a range
```python
# sum of nums[i] to nums[j] (both included)
prefix[j + 1] - prefix[i]
# sum of nums[1..2] = prefix[3] - prefix[1] = 7 - 2 = 5  (4 + 1)
```

### common pattern (count subarrays that add up to k)
```python
count = 0
total = 0
seen = {0: 1}  # running total -> how many times we've seen it
for num in nums:
    total += num
    count += seen.get(total - k, 0)  # an earlier total we can cut off
    seen[total] = seen.get(total, 0) + 1
return count
```

works even with negative numbers (sliding window doesn't).

## stacks

**last in, first out** (like a stack of plates). you only add or remove from the top. in python, use a list.

### basic operations
```python
stack = []
stack.append(1)   # push → [1]
stack.append(2)   # push → [1, 2]
stack[-1]         # peek → 2 (look at the top)
stack.pop()       # pop → 2, stack is [1]
not stack         # True if empty
```

### when to use
- matching brackets
- undo, or going "back"
- "next greater element" type questions (monotonic stack)

### common pattern (valid parentheses)
```python
pairs = {')': '(', ']': '[', '}': '{'}
stack = []
for char in s:
    if char in pairs:
        if not stack or stack.pop() != pairs[char]:
            return False
    else:
        stack.append(char)
return not stack
```

### common pattern (monotonic stack, next warmer day)
```python
# keep indexes on the stack, temperatures going down
answer = [0] * len(temps)
stack = []
for i, t in enumerate(temps):
    while stack and temps[stack[-1]] < t:
        j = stack.pop()
        answer[j] = i - j  # days waited
    stack.append(i)
return answer
```

## queues

**first in, first out** (like a line at a store). use `deque`, since `list.pop(0)` is slow.

### basic operations
```python
from collections import deque
queue = deque()
queue.append(1)    # add to back → [1]
queue.append(2)    # add to back → [1, 2]
queue.popleft()    # remove from front → 1
queue[0]           # peek front
len(queue)
```

### when to use
- breadth-first search (bfs) on trees and graphs
- processing things in the order they arrived

## binary search

find something in a **sorted** list by cutting the search space in half each step. O(log n).

### template
```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1   # target is in the right half
    else:
        right = mid - 1  # target is in the left half
return -1
```

### built in
```python
import bisect
bisect.bisect_left([1, 3, 5], 3)   # 1 (first index where 3 fits)
bisect.bisect_right([1, 3, 5], 3)  # 2 (index after the last 3)
```

### binary search on the answer
if the question is "find the smallest x that works" and you can check if one x works, binary search over x.
```python
left, right = 1, max(piles)
while left < right:
    mid = (left + right) // 2
    if works(mid):
        right = mid      # mid works, try smaller
    else:
        left = mid + 1   # mid fails, go bigger
return left
```

## sorting

python's sort is O(n log n).

### basics
```python
nums.sort()                  # sorts in place
sorted(nums)                 # returns a new sorted list
sorted(nums, reverse=True)   # biggest first
```

### sort by a key
```python
words.sort(key=len)                           # by length
pairs.sort(key=lambda x: x[1])                # by the second item
people.sort(key=lambda p: (p.age, p.name))    # by age, then name
```

### when to use
- sorting first often makes the problem easier (two pointers, intervals, grouping duplicates)
- sorted letters make a good dict key for anagrams: `"".join(sorted("eat"))  # 'aet'`

## linked lists

a chain of nodes. each node holds a value and a pointer to the next node. no indexes, you walk from the head.

### node
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### walk the list
```python
cur = head
while cur:
    print(cur.val)
    cur = cur.next
```

### common pattern (reverse a list)
```python
prev = None
cur = head
while cur:
    nxt = cur.next   # save the next node
    cur.next = prev  # flip the pointer
    prev = cur
    cur = nxt
return prev  # new head
```

### common pattern (fast and slow pointers)
```python
# slow moves 1 step, fast moves 2 steps
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # cycle found
return False
# if there's no cycle, slow ends at the middle of the list
```

### tip: dummy node
start with a fake node in front of the head so you don't need special cases for an empty list.
```python
dummy = ListNode()
tail = dummy
# ... tail.next = node; tail = tail.next
return dummy.next
```

## recursion

a function that calls itself on a smaller version of the problem.

every recursive function needs:
1. **base case**: when to stop
2. **recursive case**: call itself on something smaller

### example (factorial)
```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case
```

### memoization (save answers you already worked out)
```python
from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

without `@cache`, `fib` repeats the same work and takes O(2ⁿ). with it, O(n).

## trees

nodes connected like a family tree. the top is the **root**, nodes with no children are **leaves**. a **binary tree** has at most 2 children per node (left and right).

### node
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### depth-first search (dfs), recursive
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### traversal orders
```python
def inorder(root):   # left, node, right (gives sorted order in a bst)
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
# preorder: node, left, right
# postorder: left, right, node
```

### breadth-first search (bfs), level by level
```python
from collections import deque
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):  # only the nodes on this level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

### binary search tree (bst)
everything on the left is smaller, everything on the right is bigger. searching takes O(log n) if the tree is balanced.
```python
def search(root, target):
    while root:
        if target == root.val:
            return root
        root = root.left if target < root.val else root.right
    return None
```

## heaps

a heap always gives you the **smallest** item fast. great for "top k" or "always grab the next smallest" problems. python's `heapq` is a **min heap**.

### basic operations
```python
import heapq
heap = []
heapq.heappush(heap, 5)  # O(log n)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heap[0]                  # 1, peek smallest, O(1)
heapq.heappop(heap)      # 1, remove smallest, O(log n)
heapq.heapify(nums)      # turn a list into a heap in place, O(n)
```

### max heap (flip the sign)
```python
heapq.heappush(heap, -5)
-heapq.heappop(heap)  # 5
```

### common pattern (k largest numbers)
```python
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)  # drop the smallest
return heap  # the k largest
```

### shortcuts
```python
heapq.nlargest(2, [5, 1, 9, 3])   # [9, 5]
heapq.nsmallest(2, [5, 1, 9, 3])  # [1, 3]
```

## intervals

problems with ranges like `[start, end]`. almost always: **sort by start first**.

### do two intervals overlap?
```python
a[0] <= b[1] and b[0] <= a[1]
```

### common pattern (merge overlapping intervals)
```python
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:                       # overlaps the last one
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
return merged
```

## greedy

make the best choice **right now** at every step and never go back. simple and fast, but only works for some problems. try a few examples to check it's right.

### common pattern (max subarray sum, kadane's algorithm)
```python
best = nums[0]
current = 0
for num in nums:
    current = max(num, current + num)  # start fresh or keep going
    best = max(best, current)
return best
```

### common pattern (jump game, can you reach the end?)
```python
reach = 0
for i, jump in enumerate(nums):
    if i > reach:
        return False  # stuck
    reach = max(reach, i + jump)
return True
```

## backtracking

try every option, and **undo** your choice when you go back. used for "find all combinations / subsets / permutations".

### template
```python
def backtrack(path, choices):
    if done:
        result.append(path[:])  # save a copy
        return
    for choice in choices:
        path.append(choice)     # choose
        backtrack(path, ...)    # explore
        path.pop()              # undo
```

### common pattern (all subsets)
```python
result = []
def backtrack(start, path):
    result.append(path[:])
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
backtrack(0, [])
return result
# [1, 2] → [[], [1], [1, 2], [2]]
```

### common pattern (all permutations)
```python
result = []
def backtrack(path, used):
    if len(path) == len(nums):
        result.append(path[:])
        return
    for i in range(len(nums)):
        if not used[i]:
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
backtrack([], [False] * len(nums))
return result
```

usually slow (O(2ⁿ) or O(n!)), so it's for small inputs.

## graphs

nodes (**vertices**) connected by **edges**. trees are a special kind of graph. graphs can have cycles, so keep a `visited` set.

### adjacency list (most common way to store one)
```python
from collections import defaultdict
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)  # leave this out if edges are one-way
```

### dfs
```python
visited = set()
def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor)
```

### bfs (finds the shortest path when every edge counts as 1)
```python
from collections import deque
def bfs(start):
    visited = {start}
    queue = deque([(start, 0)])  # (node, distance)
    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
```

### grids are graphs too
```python
rows, cols = len(grid), len(grid[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for dr, dc in directions:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        ...  # (nr, nc) is a valid neighbor
```

### common pattern (number of islands)
```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"  # mark as visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1
    return count
```

### topological sort (order tasks that depend on each other)
```python
from collections import deque
indegree = {node: 0 for node in range(n)}
for a, b in edges:  # a must come before b
    indegree[b] += 1
queue = deque([node for node in indegree if indegree[node] == 0])
order = []
while queue:
    node = queue.popleft()
    order.append(node)
    for neighbor in graph[node]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)
# if len(order) < n, there's a cycle
```

### shortest path with weights (dijkstra)
```python
import heapq
def dijkstra(graph, start):  # graph[node] = [(neighbor, weight), ...]
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float("inf")):
            continue  # old entry, skip
        for neighbor, weight in graph[node]:
            new_d = d + weight
            if new_d < dist.get(neighbor, float("inf")):
                dist[neighbor] = new_d
                heapq.heappush(heap, (new_d, neighbor))
    return dist
```

## dynamic programming

break a problem into smaller problems, solve each **once**, and reuse the answers. it's recursion + memoization, or a table filled in a loop.

use it when:
- the question asks for a **count** of ways, or a **min / max**
- the answer for `n` depends on answers for smaller `n`

### steps
1. what does `dp[i]` mean? (say it in words)
2. how does `dp[i]` use smaller answers? (the formula)
3. what are the starting values? (base cases)
4. where is the final answer?

### example (climbing stairs, 1 or 2 steps at a time)
```python
# dp[i] = number of ways to reach step i
dp = [0] * (n + 1)
dp[0], dp[1] = 1, 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
return dp[n]
```

### example (house robber, can't rob two houses in a row)
```python
# prev = best total up to two houses back, cur = best up to the last house
prev, cur = 0, 0
for money in nums:
    prev, cur = cur, max(cur, prev + money)  # skip it, or rob it
return cur
```

### example (coin change, fewest coins)
```python
# dp[a] = fewest coins to make amount a
dp = [0] + [float("inf")] * amount
for a in range(1, amount + 1):
    for coin in coins:
        if coin <= a:
            dp[a] = min(dp[a], dp[a - coin] + 1)
return dp[amount] if dp[amount] != float("inf") else -1
```

### 2d dp (longest common subsequence)
```python
# dp[i][j] = answer for a[:i] and b[:j]
dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
return dp[len(a)][len(b)]
```

## tries

a tree for words, one letter per level. great for "does any word start with ...?" (prefix) problems.

### template
```python
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node["#"] = True  # marks the end of a word

    def search(self, word):
        node = self._find(word)
        return node is not None and "#" in node

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def _find(self, s):
        node = self.root
        for char in s:
            if char not in node:
                return None
            node = node[char]
        return node
```

## which pattern to use

| if the problem says... | try |
|---|---|
| "have I seen this before?" / count things | hashmaps, sets |
| sorted array, find a pair | two pointers |
| longest / shortest **continuous** subarray or substring | sliding window |
| sum of a range, subarrays that add up to k | prefix sums |
| matching brackets, "next greater" | stack |
| sorted, or "smallest x that works" | binary search |
| top k, k-th largest, always need the smallest | heap |
| overlapping ranges | sort + intervals |
| all combinations / subsets / permutations | backtracking |
| connected things, islands, shortest steps | graphs (bfs / dfs) |
| tasks that depend on other tasks | topological sort |
| count the ways, min / max with choices | dynamic programming |
| word prefixes | trie |
