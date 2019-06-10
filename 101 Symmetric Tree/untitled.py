class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root:
            return self.isSameTree(root.left, root.right)
        return True

    def isSameTree(self, p, q):
        if p and q:
            q.left, q.right = q.right, q.left
            if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
        elif not p and not q:
            return True
        else:
            return False


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
    r = build_tree([1,2,2,None,3,None,3])
    print_tree(r)
    print(sol.isSymmetric(r))
