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

# neat tricks

set(): collection of unique items, store multiple items in a single variable and it removes any duplicate items
useful if we want to see unique numbers, check if there is an item that exists in a collection