class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1000000000)
        dummy.next = head
        prev = dummy
        while head:
            if head.val > prev.val:
                head = head.next
                prev = prev.next
                continue
            cur = dummy
            while cur.next and head.val > cur.next.val:
                cur = cur.next
            if head != cur.next:
                tmp = head.next
                head.next = cur.next
                cur.next = head
                prev.next = tmp
                head = tmp
            else:
                head = head.next
                prev = prev.next
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
    l = new_ll([1])
    print_ll(sol.insertionSortList(l))

