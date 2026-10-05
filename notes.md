# arrays

list of items stored in order. you access items by index.

create an array:
```python
array = [1, 2, 3]
```

access an item:
```python
print(array[2])  # 3
```

add item:
```python
array.append(6)  # [1, 2, 3, 6]
```

remove item:
```python
del array[0]
```

update item:
```python
array[1] = 10
```

iterate:
```python
for item in array:
    print(item)
```

find length:
```python
len(array)
```

# hashing

hashing is a way to quickly find items in a collection. it uses a hash function ("secret formula") to compute a unique index (or "hash") for each item.

- **direct access**: with the hash function, you can jump straight to where an item lives, so lookups are fast.
- **use case**: hashing is great when you need to look up items in a big collection a lot. that's why hash tables use it, for fast access to data.

create a dictionary:
```python
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
```

access an item:
```python
my_dict['banana']  # 2
```

add item:
```python
my_dict['date'] = 4
```

remove item:
```python
del my_dict['apple']  # {'banana': 2, 'cherry': 3, 'date': 4}
```

update item:
```python
my_dict['banana'] = 15  # {'banana': 15, 'cherry': 3, 'date': 4}
```

iterate:
```python
# go through the dictionary and print each key-value pair
for key, value in my_dict.items():
    print(key, value)
# output:
# banana 15
# cherry 3
# date 4
```

get all keys:
```python
my_dict.keys()  # dict_keys(['banana', 'cherry', 'date'])
```

get all values:
```python
my_dict.values()  # dict_values([15, 3, 4])
```

# strings

sequence of characters stored in order. works a lot like an array (index, slice, loop), but strings are **immutable**: you can't change a character in place, every change makes a new string.

create a string:
```python
s = "hello"
```

access a character:
```python
s[0]   # 'h'
s[-1]  # 'o' (negative index counts from the end)
```

slicing:
```python
s[1:4]   # 'ell' (start included, end excluded)
s[:2]    # 'he'
s[2:]    # 'llo'
s[::-1]  # 'olleh' (reverse a string)
```

"update" a character:
```python
s[0] = 'j'          # error, strings are immutable
s = 'j' + s[1:]     # 'jello', make a new string instead
```

iterate:
```python
for char in s:
    print(char)

for i, char in enumerate(s):  # index + character
    print(i, char)
```

find length:
```python
len(s)  # 5
```

change case:
```python
s.upper()  # 'HELLO'
s.lower()  # 'hello'
```

check character type:
```python
'a'.isalpha()  # True, letter
'5'.isdigit()  # True, number
'a'.isalnum()  # True, letter or number (good for skipping punctuation)
' '.isspace()  # True, whitespace
```

split and join:
```python
"a b c".split()     # ['a', 'b', 'c'] (splits on whitespace)
"a,b,c".split(",")  # ['a', 'b', 'c']
"-".join(['a', 'b', 'c'])  # 'a-b-c'
```

strip whitespace:
```python
"  hi  ".strip()  # 'hi'
```

find and replace:
```python
"hello".find("l")         # 2 (first index, -1 if not found)
"hello".count("l")        # 2
"hello".replace("l", "L") # 'heLLo'
"ell" in "hello"          # True
```

convert between string and list:
```python
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']
"".join(chars)         # 'hello'
```

characters to numbers:
```python
ord('a')  # 97
chr(97)   # 'a'
ord('c') - ord('a')  # 2 (position in the alphabet, useful for arrays of size 26)
```

count characters:
```python
from collections import Counter
Counter("hello")  # {'l': 2, 'h': 1, 'e': 1, 'o': 1}
```

common pattern (build a string efficiently):
```python
# adding to a string in a loop makes a new string every time (slow)
# add to a list, then join once at the end
result = []
for char in s:
    result.append(char.upper())
"".join(result)  # 'HELLO'
```

common pattern (check palindrome):
```python
s == s[::-1]
```

# neat tricks

**set()**: collection of unique items. stores multiple items in a single variable and removes any duplicates.

- useful if we want to see unique numbers
- useful to check if an item exists in a collection

create a set:
```python
my_set = {1, 2, 3}
empty_set = set()  # {} makes a dict, not a set
```

remove duplicates from a list:
```python
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)  # {1, 2, 3}
```

add item:
```python
my_set.add(4)  # {1, 2, 3, 4}
my_set.add(2)  # already there, nothing changes
```

remove item:
```python
my_set.remove(4)   # error if 4 isn't in the set
my_set.discard(9)  # no error if 9 isn't in the set
```

check if item exists:
```python
if 2 in my_set:  # fast lookup, like a dictionary
    print("found")
```

find length:
```python
len(my_set)  # 3
```

iterate:
```python
# sets have no order, so the output order isn't guaranteed
for item in my_set:
    print(item)
```

common pattern (check for duplicates):
```python
seen = set()
for num in nums:
    if num in seen:
        return True
    seen.add(num)
return False
```

# two pointers

```python
left = 0
right = len(nums) - 1
while left < right:
    total = nums[left] + nums[right]

    if total == result:
        return True
    elif total < result:
        left += 1
    else:
        right -= 1
return False
```

# sliding window

we use it when we care about a **continuous section** of an array or string.

- **fixed-size window**: window stays the same size.
  - example: "maximum sum of 3 consecutive numbers"
- **variable-size window**:
  - right → expands the window
  - left → shrinks the window when needed
  - example: "longest substring without duplicates"

python template:
```python
left = 0

for right in range(len(nums)):
    # expand window

    while window_is_bad:
        # shrink window
        left += 1

    # update answer
```
