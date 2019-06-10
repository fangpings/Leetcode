# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
        lpath = self.pathSum(root.left, sum - root.val) if root.left else []
        rpath = self.pathSum(root.right, sum - root.val) if root.right else []
        path = [[root.val] + x for x in lpath + rpath]
        return path