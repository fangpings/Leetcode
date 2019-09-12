# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         if p == root or q == root:
#             return root
#         p_path = self.search_node(root, p)
#         q_path = self.search_node(root, q)
#         i = 0
#         cur = root
#         while i < min(len(q_path), len(p_path)) and q_path[i] == p_path[i]:
#             if q_path[i] == 0:
#                 cur = cur.left
#             else:
#                 cur = cur.right
#         return cur

#     def search_node(self, node, target):
#         if node == target:
#             return []
#         elif not node:
#             return None
#         else:
#             left = self.search_node(node.left, target)
#             right = self.search_node(node.right, target)
#             if left == None and right == None:
#                 return None
#             elif left != None:
#                 return left + [0]
#             else:
#                 return right + [1]

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.ret = None
        self.rec(root, p, q)
        return self.ret

    def rec(self, node, p, q):
        if not node:
            return False
        mid = node == p or node == q
        left = self.rec(node.left, p, q)
        right = self.rec(node.right, p, q)
        if mid + left + right == 2:
            self.ret = node
        return mid or left or right
