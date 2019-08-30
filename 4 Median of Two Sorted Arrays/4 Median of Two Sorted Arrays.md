### 4 Median of Two Sorted Arrays

There are two sorted arrays **nums1** and **nums2** of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume **nums1** and **nums2** cannot be both empty.

**Example 1:**

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

**Example 2:**

```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

### 想法

这道题的难点有两个 第一个是本身就很难想。。我们需要这么去理解median，median代表我们把这些数分成两堆，1. 这两堆的数量差不超过一 2.其中一堆的最大值小于另一堆的最小值。那么对于总数偶数个，median就是左边最大值和右边最小值的平均值，对于总数奇数个，median就是数量较多的那一堆的最大或最小值。

![IMG_4968](/Users/Kururuken/Desktop/Leetcode/4 Median of Two Sorted Arrays/IMG_4968.jpg)

第二个难点在于边界条件。。边界条件实在是太特么多了

有以下几个：1.总数是奇数还是偶数 2.i=0 or i = m 3. j=0 or j=n 4.m或n=0

其中2 3还是相伴出现的，即只有在i=0的情况下j才可能等于n（因为m<=n),只有在i=m情况下j才可能等于0