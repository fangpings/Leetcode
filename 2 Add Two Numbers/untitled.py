# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        extra = 0
        ori_node = ListNode(0)
        cur = ori_node
        while l1 and l2 :
            digit = l1.val + l2.val + extra
            digit, extra = digit % 10, digit // 10
            cur.val = digit
            if l1.next == None and l2.next == None:
                if extra:
                    cur.next = ListNode(1)
                return ori_node
            cur.next = ListNode(0)
            cur = cur.next
            l1, l2 = l1.next, l2.next
        if l1 and not l2:
            while True:
                digit = l2.val + extra
                digit, extra = digit % 10, digit // 10
                cur.val = digit
                if l2.next == None:
                    if extra:
                        cur.next = ListNode(1)
                    return ori_node
                cur.next = ListNode(0)
                cur = cur.next
                l2 = l2.next
        else:
            while True:
                digit = l1.val + extra
                digit, extra = digit % 10, digit // 10
                cur.val = digit
                if l1.next == None:
                    if extra:
                        cur.next = ListNode(1)
                    return ori_node
                cur.next = ListNode(0)
                cur = cur.next
                l1 = l1.next