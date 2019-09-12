class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        # if not root.left:
        #     return 1
        depth = 0
        cur = root
        while cur:
            depth += 1
            cur = cur.left
        current_depth = 1
        count = 0
        cur = root
        while cur:
            tmp_depth = current_depth
            tmp = cur.left
            while tmp:
                tmp_depth += 1
                tmp = tmp.right
            if tmp_depth == depth:
                count += 2 ** (max(0, depth - current_depth - 1))
                cur = cur.right
            else:
                cur = cur.left
            current_depth += 1
        return 2 ** (depth - 1) - 1 + count

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == '__main__':
    root = TreeNode(0)
    # root.left = TreeNode(0)
    # root.right = TreeNode(0)
    sol = Solution()
    print(sol.countNodes(root))

