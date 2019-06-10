class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        return self.sortedArrayToBST(l)

    def sortedArrayToBST(self, nums):
        if nums:
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = self.sortedArrayToBST(nums[:mid])
            node.right = self.sortedArrayToBST(nums[mid+1:])
            return node