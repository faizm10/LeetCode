#stacks
# using list
stack = []
stack.append(x)   # push
x = stack.pop()   # pop (raises if empty)
top = stack[-1]   # peek (if not empty)
empty = len(stack) == 0

# or deque (similar speed for stack ops)
from collections import deque
stack = deque()
stack.append(x); x = stack.pop()
