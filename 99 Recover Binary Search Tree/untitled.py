# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        self.first_wrong = None
        self.second_wrong = None
        self.morris(root)
        self.first_wrong.val, self.second_wrong.val = self.second_wrong.val, self.first_wrong.val


    def morris(self, root):
        current = root
        self.prev = TreeNode(-100000000000)
        while current != None:
            if current.left == None:
                if current.val < self.prev.val:
                    if not self.first_wrong:
                        self.first_wrong = self.prev
                        self.second_wrong = current
                    else:
                        self.second_wrong = current
                self.prev = current
                current = current.right
            else:
                prev = current.left
                while prev.right != None and prev.right != current:
                    prev = prev.right
                if prev.right == None:
                    prev.right = current
                    current = current.left
                else:
                    prev.right = None
                    if current.val < self.prev.val:
                        if not self.first_wrong:
                            self.first_wrong = self.prev
                            self.second_wrong = current
                        else:
                            self.second_wrong = current
                    self.prev = current
                    current = current.right




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
    r = build_tree([3,1,4,None,None,2])
    print_tree(r)
    sol.recoverTree(r)
    print_tree(r)