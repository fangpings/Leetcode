### 56 Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

**Example 1:**

```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:**

```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

#### 想法

先对`intervals`关于`start`排序，保证区间的起始是从小到大排的。然后我们从第一个区间开始往下搜索。我们设定当前区间的起始值为下一个加入返回值的区间的开始值。如果下一个区间的起始小于本区间的结束，那说明是有重叠(或者被完全包括)。这个时候我们取临时的下一个加入返回值的区间的结束值为两者中较大的那一个。然后把**下一个**区间的指针+1(注意直到下一个区间的开始值**大于**当前区间的结束值时才会结束内循环)。内循环结束的时候当前区间会移动到下一个区间。