### 621 Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval **n** that means between two **same tasks**, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the **least** number of intervals the CPU will take to finish all the given tasks.

**Example:**

```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B. 
```

**Note:**

1. The number of tasks is in the range [1, 10000].
2. The integer n is in the range [0, 100].

### 想法

最开始的想法是**每次操作，都优先安排剩余次数最多的任务**。这个想法本身是对的，我的做法是安排两个数组，一个ready表示当前已经冷却完毕的task任务，每次用heap找到剩余次数最多的，另一个是cool down数组，这个数组有n个slot，代表0到n的冷却时间，每当下一个时间节点，最左边0冷却时间的任务加入ready，同时当前step决定的任务加入cooldown最右边的n冷却时间。这样的时间复杂度实际上是O(time)（我觉得这个做法已经挺巧妙的了。。无奈有更牛逼的）

如果我们顺在刚刚的想法更进一步，就会发现**最后的操作时间其实只和次数最多的任务有关**。再有一点就是**最后的总任务时间就是任务的个数加上idle的次数，所以我们要计算的就是idle的次数**。而idle的次数只和总任务的次数有关，更进一步，只和最多的任务次数有关

```
A # # # A # # # A # # # A
```

假设A是出现次数最多的任务，那么最后的任务分配情况一定是这样的（有一个例外，但是不影响，下面会解释）。这里的每个含A的section数目就是n+1，而总的section数目是max_freq - 1.这样我们只需要关心剩下的任务填不填的满这些#号了，如果填满还不够，那最后时间数就是总任务次数，如果填不满，那最后的任务次数就是这里的总次数。

有一个例外就是有最大数目的任务有很多个，这里也分两种情况，第一种情况是最大任务的数目不到n，那每个section的length还是n+1,但是如果最大任务的数目超过n了，那section的length就应该取最大任务的数目。

总结起来就是这三行

```python
sections = max_freq - 1
sections_length = max(n+1, max_count)
return max(len(tasks), sections * sections_length + max_count)
```

