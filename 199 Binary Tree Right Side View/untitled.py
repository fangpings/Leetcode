# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        another = []
        ret = []
        while True:
            while queue:
                last = queue.pop(0)
                if last.left:
                    another.append(last.left)
                if last.right:
                    another.append(last.right)
            ret.append(last.val)
            if not another:
                return ret
            else:
                queue = another
                another = []


