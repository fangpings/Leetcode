class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def rec(head, sentinel):
            if not head or head.val == sentinel:
                return head
            dummy = ListNode(0)
            dummy.next = head
            cur = head
            pivot = head
            while cur.next and cur.next.val != sentinel:
                if cur.next.val == pivot.val:
                    if cur == pivot:
                        cur = cur.next
                        pivot = pivot.next
                    else:
                        tmp = cur.next
                        cur.next = tmp.next
                        tmp.next = pivot.next
                        pivot.next = tmp
                        pivot = pivot.next
                elif cur.next.val < pivot.val:
                    tmp = cur.next
                    cur.next = tmp.next
                    tmp.next = dummy.next
                    dummy.next = tmp
                else:
                    cur = cur.next
            dummy.next = rec(dummy.next, pivot.val)
            pivot.next = rec(pivot.next, sentinel)
            return dummy.next
        return rec(head, None)

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
    l = new_ll([4,3,2,1])
    print_ll(sol.sortList(l))


