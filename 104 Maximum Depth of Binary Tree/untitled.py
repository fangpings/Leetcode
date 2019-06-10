class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        rootd = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return rootd

def build_tree(l):
    def rec(k):
        if k - 1 < len(l):
            if l[k-1]:
                node = TreeNode(l[k-1])
                node.left = rec(2*k)
                node.right = rec(2*k+1)
                return node
            else:
                l.insert(2*k-1, None)
                l.insert(2*k, None)
                return None
    return rec(1)

if __name__ == '__main__':
    sol = Solution()
    r = build_tree([3,9,20,None,None,15,7])
    print(sol.maxDepth(None))
