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

#
#to find max depth of binary tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0                      # base (nodes)
        L = self.maxDepth(root.left)
        R = self.maxDepth(root.right)
        return 1 + max(L, R)