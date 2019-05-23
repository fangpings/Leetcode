def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 and not l2:
        return None
    head = ListNode(0)
    cur = head
    while l1 and l2:
        if l1 < l2:
            cur.next = ListNode(l1.val)
            l1 = l1.next
        else:
            cur.next = ListNode(l2.val)
            l2 = l2.next
        cur = cur.next
    if not l1:
        while l2:
            cur.next = ListNode(l2.val)
            l2 = l2.next
    else:
        while l1:
            cur.next = ListNode(l1.val)
            l1 = l1.next
    return head.next

