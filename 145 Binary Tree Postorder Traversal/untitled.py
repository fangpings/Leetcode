class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [(root, 0)]
        ret = []
        while stack:
            node, status = stack[-1]
            if status == 0:
                if node.left:
                    stack[-1] = (node, 1)
                    stack.append((node.left, 0))
                elif node.right:
                    stack[-1] = (node, 2)
                    stack.append((node.right, 0))
                else:
                    stack[-1] = (node, 2)
            elif status == 1:
                if node.right:
                    stack[-1] = (node, 2)
                    stack.append((node.right, 0))
                else:
                    stack[-1] = (node, 2)
            elif status == 2:
                stack.pop()
                ret.append(node.val)
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
    r = build_tree([1,2,3,4,5,6,7])
    print(sol.preorderTraversal(r))