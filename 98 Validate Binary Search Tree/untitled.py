# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        def rec(node, lower, upper):
            if not lower < node.val < upper:
                return False
            left_flag = (node.left and rec(node.left, lower, node.val)) or not node.left
            right_flag = (node.right and rec(node.right, node.val, upper)) or not node.right
            return left_flag and right_flag
        if not root:
            return True
        return rec(root, -10000000000, 10000000000)

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
    print_tree(build_tree([5,1,4,None,None,3,6]))
    print(sol.isValidBST(build_tree([5,1,4,None,None,3,6])))




