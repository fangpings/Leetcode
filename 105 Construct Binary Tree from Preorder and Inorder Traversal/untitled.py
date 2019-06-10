class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

class Solution:
    def buildTree(self, preorder, inorder):
        def build(stop):
            if inorder and inorder[0] != stop:
                root = TreeNode(preorder.pop(0))
                root.left = build(root.val)
                inorder.pop(0)
                root.right = build(stop)
                return root
        return build(None)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

if __name__ == '__main__':
    sol = Solution()
    r = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
    print_tree(r)
