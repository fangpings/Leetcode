### 445 Add Two Numbers II

You are given two **non-empty** linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Follow up:**
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

**Example:**

```
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```

### 想法

这情况和 Add Two Numbers I 完全不一样了。这回直接先把两个数算出来比较方便，然后加在一起再重新生成一个新的list就行。

```python
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
```

