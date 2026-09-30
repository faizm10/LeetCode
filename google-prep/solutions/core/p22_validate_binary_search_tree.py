"""
p22. Validate Binary Search Tree (Medium)
Topic: Trees

Given the root of a binary tree, return True if it is a valid binary
search tree (every node's value strictly greater than all values in its
left subtree and strictly less than all values in its right subtree).

Example:
Input: root = [2,1,3]
Output: True

Input: root = [5,1,4,null,null,3,6]
Output: False   (4's right child 3 is less than 4's parent 5... actually
                  4 < 5 but 3 < 4, violating the right-subtree constraint
                  relative to the root)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                queue.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                queue.append(node.right)
    return root


def is_valid_bst(root):
    def helper(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)

    return helper(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    assert is_valid_bst(build_tree([2, 1, 3])) is True
    assert is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])) is False
    assert is_valid_bst(None) is True
    assert is_valid_bst(build_tree([1])) is True
    assert is_valid_bst(build_tree([10, 5, 15, None, None, 6, 20])) is False
    print("All tests passed!")
