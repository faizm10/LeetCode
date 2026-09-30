# Python DSA & Algorithms — Offline Coding Exercise Guide

Prepared for Faiz • Python 3 • Google Software Developer Intern preparation

Use this as an offline study reference. The patterns are general preparation, not predictions of Google's questions. For the actual assessment, follow its rules on reference materials and assistance.

## Contents
1. Solving workflow and 90-minute strategy
2. Complexity and choosing an approach
3. Python essentials and data structures
4. Pattern recognition
5. Arrays, hashing, prefix sums, two pointers, sliding windows
6. Sorting, intervals, binary search, heaps, stacks
7. Linked lists, trees, graphs, shortest paths, union-find
8. Backtracking, dynamic programming, tries, bits and math
9. Worked examples
10. Debugging and offline practice

## 1. Solving workflow

For every problem:
1. Restate exactly what must be returned: count, length, indices, path, boolean, or optimal value.
2. Read constraints. Are values negative? Are duplicates allowed? Is input sorted? Can it be empty?
3. Work a tiny example manually.
4. Describe brute force and its complexity.
5. Identify repeated work and choose a pattern.
6. State an invariant: what remains true while the algorithm runs?
7. Implement the simplest correct solution fitting the constraints.
8. Test boundaries and estimate time/space.

Quick planning scratchpad:
```text
Input / output:
Constraints / assumptions:
Brute force:
Repeated work:
Chosen pattern / invariant:
Time / space:
Edge cases:
```

### 90-minute, two-problem exercise
| Minutes | Goal |
|---|---|
| 0–5 | Read both; start with the clearer problem if navigation permits. |
| 5–15 | Derive approach to problem 1. |
| 15–35 | Implement problem 1. |
| 35–40 | Test and move on. |
| 40–50 | Derive approach to problem 2. |
| 50–75 | Implement and test problem 2. |
| 75–85 | Review correctness and performance of both. |
| 85–90 | Submit and confirm completion through the platform. |

After eight minutes with no progress, write brute force and identify its repeated work. Switch problems if still blocked and allowed. A working slower solution can be a useful baseline; passing samples does not establish that it meets full constraints.

Confirmed calendar instructions: deadline October 6, 2026, 3:59 PM Japan time; 90 minutes, two problems; practice first; use the same email account as first access; timer begins at “Start timed exercise.” Aim to finish October 5. The deadline reminder is not a start time. Accommodations: assessment-help@google.com before starting, subject containing [Scaled Assessment].

## 2. Complexity

| Complexity | Typical example |
|---|---|
| O(1) | Array index lookup |
| O(log n) | Binary search |
| O(n) | One scan; each element pushed/popped once |
| O(n log n) | Comparison sorting |
| O(n²) | All pairs; all subarrays with incremental sums |
| O(2ⁿ) | Enumerating subsets |
| O(n!) | Enumerating permutations |

Rough feasibility clues, not guarantees: n near 20 may permit subsets; n near 1,000 may permit quadratic work; n near 100,000 usually calls for O(n) or O(n log n). Actual limits depend on time limits, language, constants and operations. A loop within a loop is not always quadratic: two pointers that each move only forward can total O(n).

Count all input dimensions. A grid traversal is O(rows × columns); adjacency-list graph traversal is O(V + E). Space includes visited sets, queues, tables and recursion depth. State whether output space is included.

## 3. Python essentials

```python
from collections import Counter, defaultdict, deque
from heapq import heapify, heappush, heappop
from bisect import bisect_left, bisect_right
from functools import cache
from math import gcd, isqrt, inf

# Lists / iteration
a = [3, 1, 3]
a.append(5)
last = a.pop()
for i, value in enumerate(a):
    pass
for x, y in zip([1, 2], [3, 4]):
    pass
for i in range(len(a) - 1, -1, -1):
    pass

# Hashing
counts = Counter(a)                 # {3: 2, 1: 1}
freq = {}
freq[3] = freq.get(3, 0) + 1
seen = set(a)
seen.add(9)
seen.discard(8)                     # no error if absent
groups = defaultdict(list)
groups['key'].append(1)

# Sorting
ordered = sorted(a)                # new list
a.sort()                           # mutates, returns None
pairs = [(2, 5), (1, 9)]
pairs.sort(key=lambda pair: (pair[0], -pair[1]))

# Queue and stack
q = deque([1])
q.append(2)
first = q.popleft()
stack = []
stack.append(1)
top = stack[-1]
stack.pop()

# Heap: min-heap
heap = [4, 1, 7]
heapify(heap)
heappush(heap, 2)
smallest = heappop(heap)
# Max-heap compatible with older Python versions: store negative priorities.

# Strings
text = ''.join(['a', 'b', 'c'])
parts = 'a b c'.split()
letters = list(text)
alphabet_index = ord('c') - ord('a')

# Independent grid rows
grid = [[0] * 4 for _ in range(3)]
```

| Structure / operation | Cost / use |
|---|---|
| list index; append/pop at end | O(1) index, amortized O(1) append, O(1) end pop |
| list insert/pop at front | O(n); use deque for queues |
| `x in list` | O(n) |
| dict/set lookup, insert, delete | Expected O(1); hashable keys required |
| deque append/pop either end | O(1) |
| heap push/pop | O(log n); root lookup O(1); heapify O(n) |
| sorted list bisect | O(log n) search; insertion still O(n) |
| list/string slicing | O(slice length); makes a copy |
| sorting | O(n log n); Python sorting is stable |

### Python traps
- `[[0] * cols] * rows` shares the same row; use a comprehension.
- `a.sort()` returns None. `a = a.sort()` destroys your reference.
- `/` returns a float; `//` floors. With negatives, flooring differs from truncation toward zero.
- Strings are immutable. Build a list and join when creating many characters.
- Use tuples, not lists, as set members or dictionary keys.
- `dict.get(key, default)` does not insert the key. `defaultdict` indexing may insert it.
- Avoid changing dictionary/set size while iterating over it.
- `if answer:` rejects zero. Use `if answer is not None:` when zero is valid.
- Python integers grow as needed; other languages may need 64-bit integers for sums/counts.
- Long recursive chains can exceed Python's recursion limit; prefer iterative traversal for large inputs.
- Respect the supplied function signature and return format. Only parse stdin if requested.

## 4. Pattern recognition

| Signal | Consider | Check before choosing |
|---|---|---|
| Pair matching a target | Hash map; sorted two pointers | Return original indices? |
| Count frequencies / duplicates | Counter, set, dictionary | Is multiplicity important? |
| Contiguous sum, including negatives | Prefix sums + map | Count versus longest length? |
| Longest valid contiguous segment | Sliding window | Does shrinking restore validity monotonically? |
| Sorted pair / palindrome | Two pointers | Is sorting allowed to change order? |
| Overlapping intervals | Sort + merge / sweep / heap | Are endpoints inclusive? |
| First feasible value | Binary search on answer | Is feasibility monotone? |
| Repeated smallest / largest | Heap | Fixed top-k or dynamic process? |
| Next greater / smaller | Monotonic stack | Strict versus non-strict comparison? |
| Reachability / components | DFS or BFS | Directed or undirected? |
| Minimum unweighted steps | BFS | What information belongs in each state? |
| Nonnegative weighted shortest path | Dijkstra | Negative edges invalidate this template. |
| Prerequisites | Topological sort | Can cycles exist? |
| Repeated connectivity / merging | Union-find | Cannot directly handle arbitrary deletions. |
| Enumerate combinations | Backtracking | Can branches be pruned? |
| Optimal result from overlapping smaller problems | DP | What state completely defines the remainder? |

Subarray/substring = contiguous. Subsequence = order preserved but gaps allowed. Subset = selection; order usually irrelevant. Confusing these changes the algorithm.

## 5. Arrays and hashing

### Two sum — O(n) expected time, O(n) space
```python
def two_sum(nums, target):
    seen = {}  # value -> earlier index
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
```
Look up before inserting so you cannot reuse the current index. Example `[3,3]`, target 6 -> `[0,1]`.

### Prefix sums — static range queries
```python
def prefix_sums(nums):
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    return prefix
# Sum of nums[left:right], right exclusive: prefix[right] - prefix[left]
```
O(n) construction; O(1) query; O(n) space. Not efficient for frequent point updates.

### Count subarrays with sum k
```python
def count_sum_k(nums, k):
    freq = {0: 1}
    total = answer = 0
    for x in nums:
        total += x
        answer += freq.get(total - k, 0)
        freq[total] = freq.get(total, 0) + 1
    return answer
```
Expected O(n) time, O(n) space. Query before insertion. The empty prefix allows ranges starting at index 0. Works with negatives. For the longest subarray with sum k, store the earliest index of each prefix instead of its frequency; initialize `{0: -1}`.

### Two pointers on sorted input
```python
def pair_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1
    return []
```
O(n) time, O(1) extra space; sorted input required. Sorting beforehand adds O(n log n) and loses original index positions unless tracked.

### Fixed-size window
```python
def max_window_sum(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError('k must be between 1 and n')
    current = sum(nums[:k])
    best = current
    for right in range(k, len(nums)):
        current += nums[right] - nums[right - k]
        best = max(best, current)
    return best
```
O(n) time; this implementation's initial slice uses O(k) temporary space. Fixed-size sum windows work with negative numbers too.

### Variable window — longest substring without repeats
```python
def longest_unique(s):
    last = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last:
            left = max(left, last[ch] + 1)
        last[ch] = right
        best = max(best, right - left + 1)
    return best
```
Expected O(n) time, O(distinct characters) space. Invariant: `s[left:right+1]` has no repeated characters. `max` prevents left from moving backward on `abba`.

### Minimum length with sum at least target — positive values only
```python
def min_length_at_least(nums, target):
    # Requires target > 0 and every value > 0.
    left = total = 0
    best = len(nums) + 1
    for right, x in enumerate(nums):
        total += x
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == len(nums) + 1 else best
```
O(n) time, O(1) space. With negatives, this shrinking rule can miss solutions; the general version requires a different technique, such as prefix sums with a monotonic deque.

### Difference array — many inclusive range additions
```python
def apply_updates(n, updates):
    diff = [0] * (n + 1)
    for left, right, value in updates:
        diff[left] += value
        diff[right + 1] -= value
    result = []
    total = 0
    for i in range(n):
        total += diff[i]
        result.append(total)
    return result
```
Assumes `0 <= left <= right < n`. O(n + number of updates) time, O(n) space.

## 6. Sorting, searching and ordered structures

### Merge intervals
```python
def merge_intervals(intervals):
    merged = []
    for start, end in sorted(intervals):
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged
```
O(n log n) time, O(n) space. This merges intervals touching at an endpoint. For half-open intervals that should remain separate when touching, change the boundary comparison according to the specification.

### Greedy interval scheduling
To maximize the number of non-overlapping half-open intervals, sort by end time and repeatedly take the next interval whose start is at least the last selected end. Earliest finish leaves the most room for future selections. This does not solve weighted interval scheduling; that usually needs DP.

### Binary search — lower bound
```python
def lower_bound(nums, target):
    left, right = 0, len(nums)  # search interval [left, right)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```
Returns first index with value >= target, or n. O(log n) time, O(1) space. `bisect_left` does the same; `bisect_right` finds first value > target. Verify `index < n` and equality when checking membership.

### Binary search on the answer — shipping capacity
```python
def min_capacity(weights, days):
    # Nonempty positive weights, days >= 1; preserve package order.
    def feasible(capacity):
        used_days, load = 1, 0
        for weight in weights:
            if load + weight > capacity:
                used_days += 1
                load = 0
            load += weight
        return used_days <= days

    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
```
Capacity feasibility is monotone: if capacity c works, any larger capacity works. O(n log R) time where R is the integer search range (at least 1); O(1) extra space. Confirm feasible bounds before copying this pattern.

### Top k largest — bounded min-heap
```python
def top_k(nums, k):
    if k <= 0:
        return []
    heap = []
    for x in nums:
        heappush(heap, x)
        if len(heap) > k:
            heappop(heap)
    return sorted(heap, reverse=True)
```
O(n log(k+1) + k log k) time when k <= n; O(k) space. Root is the smallest among retained candidates. Duplicates are retained. Heap tuples compare subsequent fields on ties: use a numeric tie-breaker if payload objects cannot be compared.

### Meeting rooms — half-open [start, end), positive duration
```python
def min_rooms(intervals):
    ends = []
    best = 0
    for start, end in sorted(intervals):
        while ends and ends[0] <= start:
            heappop(ends)
        heappush(ends, end)
        best = max(best, len(ends))
    return best
```
O(n log n) time, O(n) space. A meeting ending at t frees a room for one starting at t.

### Monotonic stack — next strictly greater value
```python
def next_greater(nums):
    answer = [-1] * len(nums)
    stack = []  # indices awaiting a greater value
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            answer[stack.pop()] = x
        stack.append(i)
    return answer
```
O(n) time and space: each index is pushed and popped at most once. Store indices if the output needs distances. Equality stays on the stack for strictly greater queries.

### Balanced brackets
```python
def valid_brackets(s):
    match = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in match:
            if not stack or stack.pop() != match[ch]:
                return False
    return not stack
```
O(n) time, O(n) space. This ignores non-bracket characters; change if the prompt says otherwise.

## 7. Linked lists, trees and graphs

### Linked-list reversal
```python
def reverse_list(head):
    previous = None
    current = head
    while current:
        following = current.next
        current.next = previous
        previous = current
        current = following
    return previous
```
O(n) time, O(1) extra space. Save the following node before changing the pointer.

### Cycle detection — fast and slow pointers
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```
O(n) time, O(1) space. Compare node identity, not stored values.

### Tree traversals
Preorder = node, left, right. Inorder = left, node, right. Postorder = left, right, node. Inorder of a valid BST is sorted (subject to the problem's duplicate rule).
```python
def inorder(root):
    result, stack = [], []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

def tree_height(root):
    if root is None:
        return 0  # height measured in nodes here
    return 1 + max(tree_height(root.left), tree_height(root.right))
```
Both O(n) time; traversal working stack O(height), output O(n). Recursive height uses O(height) call space and can overflow on a deep tree.

### Graph construction
```python
def build_graph(n, edges, directed=False):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph
```
O(V + E) time and space. Check whether vertices are 0-based or 1-based.

### BFS — unweighted distances
```python
def bfs_distances(graph, start):
    distance = [-1] * len(graph)
    distance[start] = 0
    q = deque([start])
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                q.append(neighbor)
    return distance
```
O(V + E) time, O(V) auxiliary space. Mark visited when enqueuing, not when dequeuing, to avoid duplicate queue entries. For a path, store `parent[neighbor] = node` on discovery and walk backward from the destination.

### DFS — reachability
```python
def reachable(graph, start):
    seen = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return seen
```
O(V + E) time, O(V) auxiliary space. For components, start traversal at every still-unvisited vertex. DFS alone does not guarantee shortest paths.

### Grid BFS with one obstacle removal
```python
def shortest_route(grid):
    # Rectangular, nonempty 0/1 grid; start and destination open.
    rows, cols = len(grid), len(grid[0])
    q = deque([(0, 0, 0, 0)])  # row, col, removal used, moves
    seen = {(0, 0, 0)}
    while q:
        row, col, used, moves = q.popleft()
        if (row, col) == (rows - 1, cols - 1):
            return moves
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                next_used = used + grid[nr][nc]
                state = (nr, nc, next_used)
                if next_used <= 1 and state not in seen:
                    seen.add(state)
                    q.append((nr, nc, next_used, moves + 1))
    return -1
```
O(rows × cols) time and space. State must include removal usage because it changes future options. With up to k removals, this direct state-space approach becomes O(rows × cols × (k+1)).

### Multi-source BFS
Put every starting source in the queue at distance 0, marking each visited. Then run normal BFS. Useful for distance to nearest source or spreading processes. Do not run a separate full BFS from every source.

### Topological sort — prerequisites
```python
def topological_order(n, edges):
    # (u, v) means u must precede v.
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    q = deque(i for i in range(n) if indegree[i] == 0)
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return order if len(order) == n else None
```
O(V + E) time and space. `None` means a cycle exists. Ordinary visited-only DFS is insufficient to detect directed cycles; use an active-path state or this indegree method.

### Dijkstra — nonnegative edge weights
```python
def dijkstra(graph, start):
    # graph[u] contains (v, weight)
    distance = [inf] * len(graph)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        cost, node = heappop(heap)
        if cost != distance[node]:
            continue  # stale heap entry
        for neighbor, weight in graph[node]:
            candidate = cost + weight
            if candidate < distance[neighbor]:
                distance[neighbor] = candidate
                heappush(heap, (candidate, neighbor))
    return distance
```
O((V + E) log(V + E)) safe general bound for this lazy-heap version; O(V + E) space. Common simple-graph bound is O((V + E) log V). Unreachable distances remain infinity. Negative weights require another algorithm. For weights only 0 or 1, consider 0–1 BFS with deque appendleft for zero-cost edges.

### Union-find — connectivity
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True
```
Near-constant amortized operations, O(n) space. A failed union can identify an undirected cycle when edges are processed. Kruskal's minimum spanning tree: sort edges by weight; accept edges whose union succeeds. MST is different from shortest paths.

## 8. Backtracking, DP and extra tools

### Subsets — choose, recurse, undo
```python
def subsets(nums):
    result, path = [], []
    def dfs(index):
        if index == len(nums):
            result.append(path.copy())
            return
        dfs(index + 1)  # exclude
        path.append(nums[index])
        dfs(index + 1)  # include
        path.pop()
    dfs(0)
    return result
```
O(n × 2ⁿ) including copied output; O(n) working recursion/path space, O(n × 2ⁿ) output space. Always copy the path before storing it. For unique combinations from duplicate values, sort and skip equal sibling choices, not every duplicate globally.

### Dynamic programming checklist
1. State: exactly what does `dp[i]` or `solve(i, ...)` mean?
2. Transition: what last choice or next choice leads to this state?
3. Base cases: empty prefix, zero amount, terminal index.
4. Evaluation order: dependencies must already be available.
5. Answer: which state represents the requested result?

Memoization explores states on demand; tabulation fills them explicitly. Complexity is usually number of states × work per state. Cache keys must include everything affecting future choices.

### House robber — choose or skip
```python
def rob(nums):
    # Nonnegative values; cannot select adjacent positions.
    two_back = one_back = 0
    for value in nums:
        current = max(one_back, two_back + value)
        two_back, one_back = one_back, current
    return one_back
```
Recurrence `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. O(n) time, O(1) space. State means best total through the current index, not necessarily including it.

### Coin change — minimum coins, unlimited reuse
```python
def min_coins(coins, amount):
    # Positive integer coins, nonnegative amount.
    dp = [inf] * (amount + 1)
    dp[0] = 0
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                dp[total] = min(dp[total], dp[total - coin] + 1)
    return -1 if dp[amount] == inf else dp[amount]
```
O(amount × number of coins) time, O(amount) space. Greedy fails for arbitrary denominations: coins `[1,3,4]`, amount 6 -> two 3s, whereas greedy takes 4+1+1.

### 0/1 knapsack — each item at most once
```python
def knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for c in range(capacity, weight - 1, -1):
            dp[c] = max(dp[c], dp[c - weight] + value)
    return dp[capacity]
```
Positive weights; equal-length input arrays; nonnegative capacity. O(n × capacity) time, O(capacity) space. Descending capacity prevents reusing the current item. Ascending capacity permits reuse and changes the problem.

### Longest increasing subsequence — strictly increasing
```python
def lis_length(nums):
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```
O(n log n) time, O(n) space. `tails[i]` is the smallest ending value found for an increasing subsequence of length i+1; `tails` itself need not be an actual subsequence. For nondecreasing length use `bisect_right`.

### Memoization skeleton
```python
def ways_to_climb(n):
    @cache
    def solve(remaining):
        if remaining == 0:
            return 1
        if remaining < 0:
            return 0
        return solve(remaining - 1) + solve(remaining - 2)
    return solve(n)
```
O(n) states/time and space for nonnegative n; recursive depth O(n). Use iterative DP for large n. Defining the cache inside the function prevents stale results across different inputs.

### Trie — prefix lookup
```python
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[None] = True  # end marker

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return None in node

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
```
Expected O(word length) insertion/search; space proportional to total stored characters. Prefix existence is different from full-word existence.

### Bits and math
```python
# Nonnegative integer bit operations
is_power_of_two = lambda x: x > 0 and (x & (x - 1)) == 0
# x & (x - 1) clears the lowest set bit.
# x & -x isolates the lowest set bit.
# x ^ x == 0; XOR cancels paired values.
# (mask >> i) & 1 reads bit i; mask | (1 << i) sets it.
# a ^ b flips bits differing between a and b.
# Python's ~x has unbounded signed behavior; mask if fixed width is needed.

def primes_up_to(n):
    if n < 2:
        return []
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for p in range(2, isqrt(n) + 1):
        if prime[p]:
            for multiple in range(p * p, n + 1, p):
                prime[multiple] = False
    return [i for i, flag in enumerate(prime) if flag]

# gcd(a,b); lcm for positive a,b = a // gcd(a,b) * b
# pow(base, exponent, modulus): efficient modular exponentiation.
# Positive integer ceiling division: (a + b - 1) // b, b > 0.
```
Sieve: O(n log log n) time, O(n) space. XOR single-number trick requires the specified pairing assumptions. Modular division is not ordinary integer division.

### Lower-priority recognition
- Fenwick tree: point updates and prefix sums in O(log n); useful when prefix sums must change.
- Segment tree: configurable range queries/updates, commonly O(log n) per operation.
- Bellman–Ford: shortest paths with negative edges; O(VE), can detect reachable negative cycles.
- Floyd–Warshall: all-pairs shortest paths; O(V³) time, O(V²) space; small graphs.
- KMP: linear string-pattern matching using a prefix-function table.
- Sweep line: sort events, maintain active state; define tie ordering carefully.
For this short preparation window, learn the core templates before implementing these advanced structures.

## 9. Worked examples

### A. Prefix sums: [1, 2, 1, 2], target 3
Earlier prefix needed = current prefix - target.
| Value | Current prefix | Needed | Earlier occurrences | Running answer |
|---|---:|---:|---:|---:|
| 1 | 1 | -2 | 0 | 0 |
| 2 | 3 | 0 | 1 | 1 |
| 1 | 4 | 1 | 1 | 2 |
| 2 | 6 | 3 | 1 | 3 |
The three ranges are indices 0..1, 1..2 and 2..3. `[0,0,0]`, target 0 has 6 nonempty subarrays; counting only distinct prefix values would undercount.

### B. Sliding window: abba
At index 0, window `a`, best 1. At index 1, `ab`, best 2. At index 2, repeated b moves left to 2, window `b`. At index 3, previous a is outside the window; left stays 2, window `ba`. Answer 2. Without `max(left, last[ch]+1)`, left would move backward and include duplicate b.

### C. Binary search capacity: [1,2,3,4,5], days 3
Bounds 5..15. Capacity 10 works: `[1,2,3,4] | [5]`; reduce upper bound to 10. Capacity 7 works: `[1,2,3] | [4] | [5]`; reduce to 7. Capacity 6 works with the same groups; reduce to 6. Capacity 5 requires 4 days: `[1,2] | [3] | [4] | [5]`; raise lower bound to 6. Answer 6.

### D. Graph state: one wall removal
For grid `[[0,1,0],[0,1,0],[0,1,0]]`, route `(0,0)->(0,1)->(0,2)->(1,2)->(2,2)` takes 4 moves. Crossing `(0,1)` consumes the removal. A cell reached with removal available is a different state from the same cell reached with it consumed.

### E. DP: robber values [2,7,9,3,1]
| Value | Best if take | Best if skip | Best total |
|---|---:|---:|---:|
| 2 | 2 | 0 | 2 |
| 7 | 7 | 2 | 7 |
| 9 | 11 | 7 | 11 |
| 3 | 10 | 11 | 11 |
| 1 | 12 | 11 | 12 |
Take uses the best result two positions back, plus current value. Answer 12 from 2+9+1.

## 10. Debugging and verification

### Test checklist
- Smallest legal input; empty input if allowed.
- One element; all equal; all zero; negatives if allowed.
- No solution; solution at first/last position; multiple valid solutions.
- Sorted and reverse-sorted input; duplicates; very large count or sum.
- Graph: disconnected vertices, cycles, self-loops if allowed.
- Grid: 1×1, one row/column, unreachable destination.
- Binary search: answer at each bound; duplicates; target absent.
- Intervals: nested, touching endpoints, identical, disjoint.

### Failure -> likely cause
| Symptom | Check |
|---|---|
| Off by one | Inclusive vs exclusive endpoints; moves vs cells; prefix index offset |
| Wrong only on zero | Truthiness; missing empty prefix; answer initialized incorrectly |
| Wrong on duplicates | Set used instead of counts; equality in stack/window rules |
| BFS too slow | Marking visited late; list.pop(0); state too large |
| Binary search hangs | Bounds do not shrink; mixing closed and half-open conventions |
| DP wrong | State definition; base case; evaluation/loop direction |
| Backtracking outputs all identical | Stored the same mutable path instead of a copy |
| Works on samples but times out | Hidden quadratic scans/slices; repeated traversal; sorting repeatedly |
| Graph misses useful paths | Visited key omitted remaining resources / other state information |

### Differential testing offline
Compare an optimized function with a simple brute-force version on many small random inputs. This checks logic more effectively than repeating samples.
```python
import random

def brute_count(nums, target):
    answer = 0
    for left in range(len(nums)):
        total = 0
        for right in range(left, len(nums)):
            total += nums[right]
            answer += (total == target)
    return answer

rng = random.Random(42)
for _ in range(1000):
    nums = [rng.randint(-3, 3) for _ in range(rng.randint(0, 10))]
    target = rng.randint(-6, 6)
    assert count_sum_k(nums, target) == brute_count(nums, target), (nums, target)
print('Prefix-sum checks passed')
```

### Offline practice set — attempt before checking hints
1. Return indices of two values adding to a target. Test `[3,3]`, target 6.
2. Count target-sum subarrays with negative values. Test `[1,-1,1]`, target 1.
3. Longest substring without repeated characters. Test `abba`.
4. Minimum length of a positive-number subarray with sum >= 7. Test `[2,3,1,2,4,3]`.
5. Merge `[[1,4],[2,3],[4,6],[8,9]]`, merging touching endpoints.
6. Minimum rooms for `[[0,30],[5,10],[15,20]]`.
7. Next greater values for `[2,1,2,4,3]`, using -1 if absent.
8. Minimum shipping capacity for `[1,2,3,4,5]` within 3 days.
9. Shortest route through `[[0,1,0],[0,1,0],[0,1,0]]` with one removal.
10. Can all courses finish with edges `[(0,1),(1,2),(2,0)]`?
11. Minimum coins for amount 6 using `[1,3,4]`.
12. Maximum non-adjacent sum for `[2,7,9,3,1]`.
13. Strict LIS length for `[10,9,2,5,3,7,101,18]`.
14. Reverse a linked list and detect a cycle independently.
15. Enumerate all subsets of `[1,2,3]`.

### Answers and pattern hints
| # | Expected result | Pattern |
|---|---|---|
| 1 | [0,1] | Hash complement |
| 2 | 3 | Prefix frequency map |
| 3 | 2 | Variable window |
| 4 | 2, from [4,3] | Positive-value shrinking window |
| 5 | [[1,6],[8,9]] | Sort + merge |
| 6 | 2 | Heap of active end times |
| 7 | [4,2,4,-1,-1] | Monotonic stack |
| 8 | 6 | Binary search on feasible capacity |
| 9 | 4 | BFS over position + removal state |
| 10 | No; cycle | Topological sort |
| 11 | 2 | Minimum-coin DP |
| 12 | 12 | Take/skip DP |
| 13 | 4 | Tails + binary search |
| 14 | Reversed pointers; boolean cycle answer | Pointer manipulation; fast/slow |
| 15 | 8 subsets | Backtracking |

### A fresh 90-minute mock
Problem A (35 minutes): Given integers, return the longest contiguous subarray with sum k. Negatives allowed; n <= 200,000. Examples: `[1,-1,5,-2,3]`, k=3 -> 4; `[-2,-1,2,1]`, k=1 -> 2. Hint: earliest prefix index. O(n) expected time.

Problem B (40 minutes): Given a grid containing 0 (empty), 1 (fresh), 2 (source), each minute sources spread to fresh orthogonal neighbors. Return minutes until all fresh cells convert, or -1. Empty cells block spreading. Example `[[2,1,1],[1,1,0],[0,1,1]]` -> 4. No fresh cells -> 0. Hint: multi-source BFS with a remaining-fresh count. O(rows × cols).

Reserve 5 minutes to read both and 10 minutes for final checks. Track where time goes. Afterward redo mistakes from memory rather than memorizing the template.

## Final quick-reference card
```text
Count exact contiguous sums + negatives -> prefix frequencies
Longest exact contiguous sum -> earliest prefix index
Longest valid substring -> window + counts / last positions
Sorted pair -> left/right pointers
Intervals -> sort; define endpoint equality
Repeated min/max -> heap
Next greater -> monotonic stack
First feasible answer -> binary search + monotone predicate
Unweighted shortest route -> BFS
Weighted nonnegative route -> Dijkstra
Prerequisites -> topological sort
Connectivity merges -> union-find
Enumerate choices -> backtracking
Overlapping smaller optimization problems -> DP
Always: constraints, invariant, boundaries, complexity, tests
```
