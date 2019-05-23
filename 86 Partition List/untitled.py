# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        fake_head = ListNode(0)
        fake_head.next = head
        par = fake_head
        while par.next is not None and par.next.val < x:
            par = par.next
        cur = par
        while cur.next is not None:
            if cur.next.val < x:
                # cur.next, par.next, cur.next.next = cur.next.next, cur.next, par.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = par.next
                par.next = tmp
                par = par.next
            else:
                cur = cur.next
        return fake_head.next

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
    sol = Solution()
    head = new_ll([3,3,3,3,1,1])
    nh = sol.partition(head, 3)
    print_ll(nh)

