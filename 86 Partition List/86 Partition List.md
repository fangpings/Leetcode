### 86 Partition List

Given a linked list and a value *x*, partition it such that all nodes less than *x* come before nodes greater than or equal to *x*.

You should preserve the original relative order of the nodes in each of the two partitions.

**Example:**

```
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
```

#### 想法

维护两个指针，第一个指向partition位置的前一个。例如当前数组是`143252`的话，指针应当指向1，第二指向当前位置，如果当前位置大于等于目标，则后移，如果小于目标，则把当前位置重新插入至第一个指针后面一位，然后第一个指针向后移动一位(第二个指针不动)