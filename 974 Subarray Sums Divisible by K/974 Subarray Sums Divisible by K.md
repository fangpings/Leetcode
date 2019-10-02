### 974 Subarray Sums Divisible by K

Given an array `A` of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by `K`.

**Example 1:**

```
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

**Note:**

1. `1 <= A.length <= 30000`
2. `-10000 <= A[i] <= 10000`
3. `2 <= K <= 10000`

### 想法

**看到subarray sum，脑子里一定要想到这个做法！。**其实和560 Subarray Sum Equals K 类似。我们规定prefix sum `p[i] = sum(nums[:i+1])`，那么所有的subarray sum就是`p[j]-p[i] for all j > i`。

于是这道题就变成了，**我们对每个`p[i]`对K取模，然后对每个值统计有多少个`p[i]`等于这个值，然后对于每个值，我们可以从所有等于他的`p[i]`中间任选两个，这两个作差一定模K为0， 那么他们构成的subarray就一定满足条件**，所以最后就变成了统计这个
$$
\sum_{i=0}^{K-1}C_{\text{nums of p[j] = i}}^2
$$
？这题能是medium？