
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_node(self):
        tmp = self
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.next

def swapPairs(head: ListNode) -> ListNode:
    new_head = ListNode(-23)
    cur = new_head
    while head and head.next:
        tmp1 = head
        tmp2 = head.next
        head = head.next.next
        cur.next = tmp2
        cur = cur.next
        cur.next = tmp1
        cur = cur.next
    if head:
        cur.next = head
    else:
        cur.next = None
    return new_head.next

if __name__ == '__main__':
    head = ListNode(-1)
    cur = head
    for i in range(3):
        cur.next = ListNode(i)
        cur = cur.next
    head = swapPairs(None)
    head.print_node()

