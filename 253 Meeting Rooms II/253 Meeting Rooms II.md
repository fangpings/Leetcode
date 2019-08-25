### 253 Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` (si < ei), find the minimum number of conference rooms required.

**Example 1:**

```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
```

**Example 2:**

```
Input: [[7,10],[2,4]]
Output: 1
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

### 想法

我们先对开会时间按照开始时间排序，然后我们开N个假想的room。如果当前meeting的开始时间比所有room的结束时间都要小，那么说明这个meeting没法安排在现有的room里面，我们就要再开一个room。

这样时间复杂度还是比较高的，如果我们利用**heap**每次找到所有room里面最小的那个结束时间再比较就行了。如果最小的结束时间还比当前的开始时间大，那么我们把当前结束时间插入堆（说明开了一个新房间），否则我们删除最小时间然后插入当前结束时间（这个房间换人了），这样就避免了遍历所有的room。时间复杂度会有所提高。**注意堆插入和删除的时间是O(logK)，K是当前房间的数量。相比前面的O(K)有所提升。**然后很神奇的一点是堆构建的时间是O(logK)