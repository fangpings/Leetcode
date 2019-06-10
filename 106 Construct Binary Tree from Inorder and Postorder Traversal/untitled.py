class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        def rec(stop):
            if inorder and inorder[-1] != stop:
                node = TreeNode(postorder.pop())
                node.right = rec(node.val)
                inorder.pop()
                node.left = rec(stop)
                return node
        return rec(None)

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
    r = sol.buildTree([9,3,15,20,7], [9,15,7,20,3])
    print_tree(r)

