# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ret = 0
        self.rec(root)
        return self.ret
    
    def rec(self, node):
        if not node:
            return -1
        left = self.rec(node.left)
        right = self.rec(node.right)
        self.ret = max(self.ret, left + right + 2)
        return max(left, right) + 1
        
        