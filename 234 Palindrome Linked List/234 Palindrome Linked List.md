### 234 Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

**Example 1:**

```
Input: 1->2
Output: false
```

**Example 2:**

```
Input: 1->2->2->1
Output: true
```

**Follow up:**
Could you do it in O(n) time and O(1) space?

### 想法

基本的想法就是先找到中点，然后reverse后半部分in place。然后一个节点一个节点对比前半部分和后半部分。

reverse是可以inplace做的，然后找中点有个比较聪明的办法，不用跑一遍半。

```python
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
```

fast每次走两格，slow每次走一格