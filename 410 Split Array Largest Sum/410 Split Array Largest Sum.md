### 410 Split Array Largest Sum

Given an array which consists of non-negative integers and an integer *m*, you can split the array into *m* non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these *m* subarrays.

**Note:**
If *n* is the length of array, assume the following constraints are satisfied:

- 1 ≤ *n* ≤ 1000
- 1 ≤ *m* ≤ min(50, *n*)

**Examples:** 

```
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
```

### 想法

最开始想到的是DP
$$
S(i, k) = \min\limits_{j}(\max(Sum(i, j), S(j+1, k-1)))
$$
这里$S(i, k)$表示从数组的$i$位置到最后，分成k个subgroup，得到的这些subgroup的最大和的最小值。于是我们需要的就是$S(0, m)$

```python
class Solution:
    def splitArray(self, nums, m):
        if m == len(nums):
            return max(nums)
        l = len(nums)
        all_sum = [[-1 for _ in range(l)] for _ in range(l)]
        for i in range(l):
            for j in range(i, l):
                all_sum[i][j] = sum(nums[i:j+1])
        s = [[0 for _ in range(m + 1)] for _ in range(l)]
        for i in range(m - 1, l):
            s[i][1] = all_sum[i][-1]
        # 下面两行其实挺精髓的，那就是我们不用遍历所有的格子，因为假设后面只有n个元素了,那么无论如何也分不出n+1个subgroup的，同理第k层的计算应该从m-k位置开始，因为还需要再分m-k个subgroup，前面至少也要留出这些空间
        for k in range(2, m + 1):
            for i in range(m - k, l - k + 1):
                s[i][k] = min([max(all_sum[i][j], s[j+1][k-1]) for j in range(i, l - k + 1)])
        return s[0][-1]
```

但是DP的时间复杂度在O(N^2*K)，还是太慢了。还有另一种超级牛逼的方法。

**我们发现这么一件事，那就是这个值一定落在这个区间里面`[max(nums), sum(nums)]`。既然他落在一个范围内，我们就反过来考虑，如果我们给出一个k，我们能不能判断m个分割能不能使得最大的subgroup的值小于等于这个k呢？如果可以，那么说明我们求的最小值一定小于等于这个k（因为有一种分割方法已经可以使这个最小值小于等于k了），如果不行，那么说明我们求的最小值一定大于这个k（k都不行，那比k小的方法更加没可能行了）**于是我们发现，如果我们找到这个判别方法，那么我们就可以做**二分搜索**了（即每次都找mid，如果mid不行，那么在右边搜索，**如果mid行，在左边搜索**（包括mid）（普通的二分如果mid行就返回了，但是这里不一样），直到left=right）。于是我们剩下的工作就是找到这个判断算法了。

现在有了给定k，其实判断算法也不难搞。**我们从头开始一直加，如果当前连续和大于k，我们就新开一组，如果不到就继续，到最后如果数组没遍历完，组数就用光了，那么说明不行，否则就说明可以。**

这一题当三题用真的是佛了。。