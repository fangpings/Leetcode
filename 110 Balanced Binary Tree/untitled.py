class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        def rec(root):
            if root:
                lh, rh = rec(root.left), rec(root.right)
                if lh >= 0 and rh >= 0 and abs(lh - rh) <= 1:
                    return max(lh, rh) + 1
                else:
                    return -1
            return 0
        if rec(root) == -1:
            return False
        return True

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
    r = build_tree([None])
    print(sol.isBalanced(r))