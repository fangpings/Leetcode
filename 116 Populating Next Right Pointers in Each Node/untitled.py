
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        save = root
        while root != None:
            next_level = Node(0, None, None, None)
            current = next_level
            while root != None:
                if root.left:
                    current.next = root.left
                    current = current.next
                if root.right:
                    current.next = root.right
                    current = current.next
                root = root.next
            root = next_level.next
        return save