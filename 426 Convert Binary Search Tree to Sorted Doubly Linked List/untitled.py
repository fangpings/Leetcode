"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        left, right = self.rec(root)
        left.left, right.right = right, left
        return left
        
    
    def rec(self, node):
        if not node:
            return None, None
        left_left, left_right = self.rec(node.left)
        right_left, right_right = self.rec(node.right)
        if not left_right:
            left_right = node
        else:
            left_right.right, node.left = node, left_right
        if not right_left:
            right_left = node
        else:
            right_left.left, node.right = node, right_left
        if not left_left:
            left_left = node
        if not right_right:
            right_right = node
        return left_left, right_right
        