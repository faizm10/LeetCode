## sliding window template

l = 0
seen = set()

for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l += 1

    seen.add(s[r])
    update answer

## two pointers template
l = 0
r = 0  # right pointer
while r < len(s):
    update answer
    r += 1

    while condition is false:
        update answer
        l += 1

    update answer
    r += 1

## hash map template
count = {}
for i in s:
    count[i] = 1 + count.get(i, 0)
    update answer

for i in t:
    count[i] -= 1
    update answer