# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        if not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False
        if root.left:
            if self.hasPathSum(root.left, sum - root.val):
                return True
        if root.right: 
            if self.hasPathSum(root.right, sum - root.val):
                return True
        return False