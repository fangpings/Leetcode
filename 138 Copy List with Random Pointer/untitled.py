# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        new_head = Node(head.val, None, None)
        head.mapping = new_head
        ptr_old = head
        ptr_new = new_head
        while ptr_old.next:
            ptr_new.next = Node(ptr_old.next.val, None, None)
            ptr_old.next.mapping = ptr_new.next
            ptr_new = ptr_new.next
            ptr_old = ptr_old.next
        ptr_old = head
        ptr_new = new_head
        while ptr_old:
            if ptr_old.random:
                ptr_new.random = ptr_old.random.mapping
            ptr_old = ptr_old.next
            ptr_new = ptr_new.next
        return new_head

if __name__ == '__main__':
    n1 = Node(-1, None, None)
    n1.random = n1
    sol = Solution()
    sol.copyRandomList(n1)