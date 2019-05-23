# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        cur = head
        pre = ListNode(0)
        pre.next = head
        new_head = pre
        while cur != None:
            if cur.next is not None and cur.next.val == cur.val:
                while cur.next is not None and cur.next.val == cur.val:
                    cur = cur.next
                cur = cur.next
                pre.next = cur
            else:
                cur = cur.next
                pre = pre.next
        return new_head.next

def new_ll(array):
    head = ListNode(0)
    cur = head
    for num in array:
        tmp = ListNode(num)
        cur.next = tmp
        cur = cur.next
    return head.next

def print_ll(head):
    while head is not None:
         print(head.val)
         head = head.next 

if __name__ == '__main__':
    head = new_ll([])
    sol = Solution()
    nh = sol.deleteDuplicates(None)
    print_ll(nh)