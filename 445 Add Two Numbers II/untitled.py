# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         c1, c2 = l1, l2
#         s1, s2 = [], []
#         while c1:
#             s1.append(c1)
#             c1 = c1.next
#         while c2:
#             s2.append(c2)
#             c2 = c2.next
#         ret = []
#         c1, c2 = len(s1) - 1, len(s2) - 1
#         prev = 0
#         while c1 >=0 and c2 >=0:
#             current_sum = prev + s1[c1].val + s2[c2].val
#             prev = current_sum // 10
#             ret.append(ListNode(current_sum % 10))
#             c1 -= 1
#             c2 -= 1
#         while c1 >= 0:
#             current_sum = prev + s1[c1].val
#             prev = current_sum // 10
#             ret.append(ListNode(current_sum % 10))
#             c1 -= 1
#         while c2 >= 0:
#             current_sum = prev + s2[c2].val
#             prev = current_sum // 10
#             ret.append(ListNode(current_sum % 10))
#             c2 -= 1
#         if prev:
#             ret.append(ListNode(1))
#         for i in range(len(ret) - 1, 0, -1):
#             ret[i].next = ret[i-1]
#         return ret[-1]

class Solution:
    def addTwoNumbers(self, l1, l2):
        n1, n2 = 0, 0
        c1, c2 = l1, l2
        while c1:
            n1 = n1 * 10 + c1.val
            c1 = c1.next
        while c2:
            n2 = n2 * 10 + c2.val
            c2 = c2.next
        total = n1 + n2
        last = None
        if total == 0:
            return ListNode(0)
        while total > 0:
            current = ListNode(total % 10)
            total //= 10
            current.next = last
            last = current
        return current
