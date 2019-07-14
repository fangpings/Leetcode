class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            tmp = stack.pop()
            ret.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
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
    sol = Solution()
    r = build_tree([3,1,2])
    print(sol.preorderTraversal(r))