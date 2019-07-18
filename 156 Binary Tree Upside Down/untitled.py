# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        stack = [(root, None)]
        while root.left:
            stack.append((root.left, root.right))
            root = root.left
        print(stack)
        left, right = stack.pop()
        ret = left
        ret.left = right
        cur = left
        while stack:
            left, right = stack.pop()
            cur.right = left
            cur = cur.right
            cur.left = right
        cur.left, cur.right = None, None
        return ret

def build_tree(l):
    root = l.pop(0)
    if not root:
        return None
    root = TreeNode(root)
    nodes = [root]
    while l != []:
        left_val = l.pop(0)
        right_val = l.pop(0) if l != [] else None
        node = nodes.pop(0)
        if left_val:
            node.left = TreeNode(left_val)
            nodes.append(node.left)
        if right_val:
            node.right = TreeNode(right_val)
            nodes.append(node.right)
    return root

def print_tree(root):
    ret = []
    q = [root]
    while q != []:
        tmp = q.pop(0)
        if tmp:
            ret.append(tmp.val)
            q.append(tmp.left)
            q.append(tmp.right)
        else:
            ret.append(None)
    print(ret)

if __name__ == '__main__':
    r = build_tree([1,2,3,4,5])
    sol = Solution()
    print_tree(sol.upsideDownBinaryTree(r))