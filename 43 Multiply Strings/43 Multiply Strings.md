### 43 Multiply Strings

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Example 1:**

```
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2:**

```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

**Note:**

1. The length of both `num1` and `num2` is < 110.
2. Both `num1` and `num2` contain only digits `0-9`.
3. Both `num1` and `num2` do not contain any leading zero, except the number 0 itself.
4. You **must not use any built-in BigInteger library** or **convert the inputs to integer** directly.

#### 想法

考虑两个数的乘法，`l1 = len(nums1), l2 = len(nums2)`,那么乘积的位数一定在`[l1+l2-1, l1+l2]`中。对于乘积的每一位，我们知道它是这么算出来的（假设加数的最右边的位置是第0位）
$$
s_i = carry + \sum_{j=max(0, i-(l_1-1))}^{min(i, l_2-1)}nums_1[i-j]*nums_2[j]
$$
例如对于`123*456`
$$
\begin{align*}
s_0 &= nums_1[0]*nums_2[0]\\
s_1 &= nums_1[1]*nums_2[0]+nums_1[0]*nums_2[1]+carry\\
s_2 &= nums_1[2]*nums_2[0]+nums_1[1]*nums_2[1]+ nums_1[2]*nums_2[0]+carry\\
s_3 &= nums_1[2]*nums_2[1]+nums_1[1]*nums_2[2]+carry\\
s_4 &= nums_1[2]*nums_2[2]+carry\\
s_5 &= carry
\end{align*}
$$
