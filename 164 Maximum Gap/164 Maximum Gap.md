### 164 Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

**Example 1:**

```
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
```

**Example 2:**

```
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
```

**Note:**

- You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
- Try to solve it in linear time/space.

### 想法

这题实在是太难想了。。特别是第一步要想到的东西。

**首先由抽屉原理,这个Max Gap的最小值一定不会小于$(max - min)/(n-1)$，这个情况是平均分布的情况，任何非平均分布的情况都只会使Max Gap变大。**

观察到这一点之后，我们就可以考虑不再去两两比较每个元素(这样的复杂度至少是nlog(n))，而是先把元素全部扔进固定个数的bucket里面，这个bucket的size小于Max Gap的最小值，这样对于每个bucket内部，我们不再需要去管它内部的gap有多大，反正不可能是答案。我们只需要维护每个bucket内部的最小值和最大值，然后用这些值计算bucket之间的gao就可以了。

bucket size我们定成$[(max - min)/(n-1)]$（向下取整），然后每个元素对应的bucket index就是`(i-min_val)//bucket_size​`。这样可以很轻松地找到对应的bucket。

