### 57 Insert Interval

Given a set of *non-overlapping* intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

**Example 1:**

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2:**

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

#### 想法

首先确定插入位置，即通过比较待插入的起始值和已有区间的结束值来确定。确定了插入位置之后，我们还要比较待插入的起始值和当前位置区间的结束值来确定是更改已有区间范围(是否和当前区间在起始值上有重复)还是要插入新的区间。再通过比较待插入区间的结束值和已有区间后面的起始值来确定结束值覆盖了哪些区间。如果确定包括某个区间，那么直接pop出这个区间就可以了。注意如果插入位置在最后，那么第二部分需要直接跳过，直接插入整个区间即可。

然后再贴一个最快的代码。很整洁

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = [interval for interval in intervals if interval[1] < newInterval[0]]
        right = [interval for interval in intervals if interval[0] > newInterval[1]]
        if left + right != intervals:
            newInterval[0] = min(newInterval[0], intervals[len(left)][0])
            newInterval[1] = max(newInterval[1], intervals[-len(right)-1][1])
        return left + [newInterval] + right
```

