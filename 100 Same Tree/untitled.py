class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        if p and q:
            if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
        elif not p and not q:
            return True
        else:
            return False

def build_tree(l):
    def rec(l, k):
        node = TreeNode(l[k-1])
        if 2 * k - 1 < len(l) and l[2 * k - 1] != None:
            node.left = rec(l, 2 * k)
        if 2 * k  < len(l) and l[2 * k] != None:
            node.right = rec(l, 2 * k + 1)
        return node
    return rec(l, 1)

def print_tree(root):
    ret = []
    q = [root]
    while q != []:
        tmp = q.pop(0)
        if tmp is not None:
            ret.append(tmp.val)
            q.append(tmp.left)
            q.append(tmp.right)
        else:
            ret.append(None)
    print(ret)

if __name__ == '__main__':
    sol = Solution()
    p = build_tree([None])
    q = build_tree([1,2,1])
    print(sol.isSameTree(p, q))
