class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while headA:
            stack1.append(headA)
            headA = headA.next
        while headB:
            stack2.append(headB)
            headB = headB.next
        while stack1 and stack2:
            pop1 = stack1.pop()
            pop2 = stack2.pop()
            if id(pop1) == id(pop2):
                last = pop1
            else:
                return last
        return None

if __name__ == '__main__':
    a = ListNode(1)
    print(id(a))