class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def rec(root):
            if root:
                rend = rec(root.right)
                lend = None
                if root.left:
                    lend = rec(root.left)
                    lend.right = root.right
                    root.right = root.left
                    root.left = None
                if rend:
                    return rend
                if lend:
                    return lend
                return root
        rec(root)

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
    sol = Solution()
    r = build_tree([1,2,5,3,4,None,6])
    print_tree(r)
    sol.flatten(r)
    print_tree(r)