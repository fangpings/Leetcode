### 829 Consecutive Numbers Sum

Given a positive integer `N`, how many ways can we write it as a sum of consecutive positive integers?

**Example 1:**

```
Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
```

**Example 2:**

```
Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
```

**Example 3:**

```
Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
```

**Note:** `1 <= N <= 10 ^ 9`.

### 想法

本质上就是个很蠢的等差数列求和，差为1，那么长度为i的等差数列，从n开始，其和要等于我们的目标x
$$
\begin{align*}
	&\frac{i*(n+(n+i-1))}{2}=x\\
	\rightleftarrows\quad&2in+i^2-i=2x\\
	\rightleftarrows\quad&n =\frac{2x+i-i^2}{2i}
\end{align*}
$$
所以只要n为整数，说明就能找到一个可行的数列了。

所以我们从i=1开始，一直找到最长的数列，最长的数列是怎么样的呢，就是从1开始的数列，所以我们带入n=1，解出i
$$
i = \frac{-1+\sqrt{1+8x}}{2}
$$
就可以了。