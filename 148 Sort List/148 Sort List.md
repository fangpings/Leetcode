### 148 Sort List

Sort a linked list in *O*(*n* log *n*) time using constant space complexity.

**Example 1:**

```
Input: 4->2->1->3
Output: 1->2->3->4
```

**Example 2:**

```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

### 想法

```
left elements: < pivot || pivot elements: = pivot || right elements: > pivot
```

还是采用和快排差不多的想法。递归的做，用链表的开始作为pivot，遍历链表，比pivot小的元素依次移到链表的开头（需要一个dummy head），比pivot大的元素不用动，等于pivot的元素移到pivot的正后方，然后pivot往后移一个位置（这里要注意，如果这个等于pivot的元素刚好就在pivot的正后方，那不能移动，直接让pivot后移，需要单独的一个判断）

做完这些之后，我们对小于pivot的元素和大于pivot的元素重新递归地做这些事情。注意我们不是数组，没办法知道index和length，那怎么办呢，我们维护一个sentinel。因为pivot元素是不会出现在小于pivot的左半边元素里面的，所以我们左半边的sentinel就是pivot了，一旦我们遇到了sentinel，说明左半边的遍历已经结束了。同理，右半边的sentinel用上级调用传进来的sentinel就行了。

最后还有一个问题就是左右半边在排完序之后，左边的连接其实是乱掉了的（右边的连接一直是正确的保持的），所以我们要恢复左边的顺利连接，所以我们这个递归函数的return值应当是左边的开始元素（dummy的next元素）

