class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        def rec(start, end):
            if start > end:
                return [None]
            ret = []
            for i in range(start, end + 1):
                left = rec(start, i - 1)
                right = rec(i + 1, end)
                for l in left:
                    for r in right:
                        tmp = TreeNode(i)
                        tmp.left = l
                        tmp.right = r
                        ret.append(tmp)
            return ret
        return rec(1, n)

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
    l = sol.generateTrees(5)
    print(len(l))



