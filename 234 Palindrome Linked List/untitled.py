class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        if count <= 1:
            return True
        mid = count // 2 + 1 if count % 2 else count // 2
        cur = head
        for _ in range(mid):
            cur = cur.next
        last = None
        while cur.next:
            last, cur.next, cur = cur, last, cur.next
        cur.next = last
        while cur:
            if cur.val != head.val:
                return False
            cur = cur.next
            head = head.next
        return True

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(sol.isPalindrome(head))