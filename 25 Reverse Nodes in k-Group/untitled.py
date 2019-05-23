class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_node(self):
        tmp = self
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    start = ListNode(-100)
    cur = start
    while True:
        stack = []
        for _ in range(k):
            stack.append(head)
            if head == None:
                cur.next = stack[0]
                return start.next
            head = head.next
        while stack != []:
            cur.next = stack.pop()
            cur = cur.next
if __name__ == '__main__':
    head = ListNode(1)
    cur = head
    for i in range(2, 6):
        cur.next = ListNode(i)
        cur = cur.next
    head = reverseKGroup(head, 5)
    head.print_node()