### 152 Maximum Product Subarray

Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

**Example 1:**

```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**

```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

#### 想法

还是用动态规划，但是重要的是要分开正负分别计算（因为负数再乘负数可能变成很大的帧数，然而我们不知道有多少个负数）。动态规划为包含当前位置i的最大正乘积和最大负乘积。如果当前位置是负数，那前一个位置的最大正乘积和当前位置的乘积（如果前一个位置是0，那就取当前位置）作为当前位置的最大负乘积，而前一个位置的最大负乘积和当前位置的乘积作为当前位置的最大正乘积（这里不用考虑0，因为前一个位置是0这一个位置也应当是0，因为当前位置是负的，不可能有最大正乘积）

动态规划的递推式如下,对于$nums[i] > 0$
$$
\begin{align*}
	plus[i] &= \max(plus[i-1] * nums[i], i)\\
	minus[i] &= minus[i-1] * nums[i]
\end{align*}
$$
对于$nums[i] < 0$
$$
\begin{align*}
	plus[i] &= minus[i-1] * nums[i]\\
	minus[i] &= \min(plus[i-1] * nums[i], nums[i])
\end{align*}
$$
对于$nums[i]=0$
$$
plus[i]=minus[i]=0
$$
然后$minus$和$plus$一开始也被初始化为0.

注意唯一可能出现答案是负数的输入是长度为1且为负数，这种情况是可以被处理的，剩下的情况都不会出现初始化的0被作为返回值的情况