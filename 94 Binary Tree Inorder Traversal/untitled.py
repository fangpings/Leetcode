class Solution:
    def inorderTraversal(self, root):
        stack = []
        ret = []
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ret.append(root.val)
            root = root.right
        return ret






