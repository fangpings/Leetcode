class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        ll = []
        tmp = head
        while tmp is not None:
            ll.append(tmp)
            tmp = tmp.next
        if len(ll) == 1:
            return head
        k = k % len(ll)
        while k > 0:
            ll[-1].next = ll[0]
            ll[-2].next = None
            ll.insert(0, ll.pop())
            k -= 1
        return ll[0]

if __name__ == '__main__':
    head = ListNode(0)
    tmp = head
    for i in range(1, 3):
        tmp.next = ListNode(i)
        tmp = tmp.next
    sol = Solution()
    new = sol.rotateRight(head, 4)
    while new != None:
        print(new.val)
        new = new.next