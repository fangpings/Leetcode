# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.path = []
        self.find_node(root, target)
        self.ret = []
        l = len(self.path)
        for i in self.path[::-1]:
            if i == 0:
                if K == l:
                    self.ret.append(root.val)
                else:
                    self.find_distance(root.right, K - l)
                root = root.left
            else:
                if K == l:
                    self.ret.append(root.val)
                else:
                    self.find_distance(root.left, K - l)
                root = root.right
            l -= 1
        self.find_distance(root, K)
        return self.ret

    def find_node(self, root, target):
        if root:
            if target == root:
                return True
            else:
                left = self.find_node(root.left, target)
                right = self.find_node(root.right, target)
                if left:
                    self.path.append(0)
                elif right:
                    self.path.append(1)
                return left or right
        return False

    def find_distance(self, root, K):
        if root and K >= 0:
            if K == 0:
                self.ret.append(root.val)
            else:
                self.find_distance(root.left, K - 1)
                self.find_distance(root.right, K - 1)

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    print(sol.distanceK(root, root.left.right, 1))
