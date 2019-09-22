### 561  Array Partition I

Given an array of **2n** integers, your task is to group these integers into **n** pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

**Example 1:**

```
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
```

**Note:**

1. **n** is a positive integer, which is in the range of [1, 10000].
2. All the integers in the array will be in the range of [-10000, 10000].

### 想法

这个就是对array排序，然后返回每两个中的第一个。也就是说pair就是从小到大每两个一组。至于这样做为什么能符合条件也很好解释，如果一组中较小的那个和另一组中较大的那个交换$(x_1, x_2), (y_1, y_2), x_2 <= y_1$，如果交换$x_1, y_2$那么$(y_1, x_2)$那组的最小值变成$X_2$变大，$(x_1, y_2)$那组最小值不变，总和变大。同理交换$x_2, y_1$也是一样。 然后如果$x_1, y_1$交换或者$x_2, y_2$交换也是一样