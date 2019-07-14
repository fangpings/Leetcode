### 143 Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where tail connects to. If `pos` is `-1`, then there is no cycle in the linked list.

**Note:** Do not modify the linked list.

 

**Example 1:**

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Example 2:**

```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Example 3:**

```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

 

**Follow-up**:
Can you solve it without using extra space?

### 想法

设置两个pointer，slow和fast，slow每次动一步，fast每次动两步。这样操作，在若干步之后，slow和fast必定相遇（为什么？因为fast每次领先slow只有一步，所以若有环，fast必定经历从slow后面到slow前面这一过程，在这一过程中因为每次只拉开一步，所以中间有一步必定相遇）

再来看会在哪里相遇？假设从HEAD到环的入口要走K步，从环的入口到相遇点slow要走X步，因为fast走的距离是slow的两倍，则fast在环内走的距离应当是2X+K，在环内的步数我们有以下的模等式
$$
X = 2X+K \pmod{C}\Rightarrow
-X = K \pmod{C}\Rightarrow
K = C - X
$$
这意味着如果在相遇之后我们重新把其中一个pointer放回起点HEAD，然后两个pointer每次均走1步，**那么K步之后两个pointer就会相遇，而且相遇的位置就是环的起点**