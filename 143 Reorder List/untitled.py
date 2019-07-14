class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        if not head:
            return
        cur = head
        storage = []
        while cur:
            storage.append(cur)
            cur = cur.next
        tail = storage.pop()
        while tail != head and tail != head.next:
            tail.next = head.next
            head.next = tail
            head = head.next.next
            tail = storage.pop()
        tail.next = None
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
    l = new_ll([1,2])
    sol.reorderList(l)
    print_ll(l)