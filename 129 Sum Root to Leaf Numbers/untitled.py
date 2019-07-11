# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        self.sum = 0
        def rec(node, pre_sum):
            if not node.left and not node.right:
                self.sum += node.val + pre_sum * 10
            if node.left:
                rec(node.left, node.val + pre_sum * 10)
            if node.right:
                rec(node.right, node.val + pre_sum * 10)
        rec(root, 0)
        return self.sum