# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        for _ in range(m - 1):
            cur = cur.next
        new_cur = cur.next
        q = [new_cur]
        for _ in range(n - m + 1):
            new_cur = new_cur.next
            q.append(new_cur)
        for node in q[::-1][1:]:
            cur.next = node
            cur = cur.next
        cur.next = q[-1]
        return dummy.next

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
    h = new_ll([1,2,3,4,5])
    nh = sol.reverseBetween(h, 1, 5)
    print_ll(nh)
