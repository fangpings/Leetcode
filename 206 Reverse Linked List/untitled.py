# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        record = []
        while head != None:
            record.append(head)
            head = head.next
        dummy = ListNode(0)
        head = dummy
        while record:
            head.next = record.pop()
            head = head.next
        head.next = None
        return dummy.next
        