class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        def rec(root):
            if not root:
                return -10000000, 0
            left_max, left_sum = rec(root.left)
            right_max, right_sum = rec(root.right)
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)
            return max(left_max, right_max, left_sum + right_sum + root.val), max(left_sum, right_sum) + root.val
        return rec(root)[0]

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
    r = build_tree([2, -1])
    print_tree(r)
    sol = Solution()
    print(sol.maxPathSum(r))
