### 221 Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

**Example:**

```
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```

### 想法

原本以为和85 Maximal Rectangle很类似，于是想用每层的histogram做，结果发现完全不一样。。

还是用DP，但是这个DP的递推式及递推式的正确性在一开始确实很难想。。

$DP[i][j]$为以i，j为右下角的最大的正方形的边长。那么我们有这样的递推式
$$
DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
$$
当然如果$nums[i][j] == 0$那么$DP[i][j] = 0$。

为什么递推式这样是对的呢，因为$DP[i-1][j-1]$确保左上角subsquare可以达到，$DP[i-1][j]$确保最右边一行可以达到，$DP[i][j-1]$确保最底下一行可以达到，这三个的最小值就确保这个正方形一定可以达到。

事实上我们还有优化空间，不需要2D的DP Matrix，只需要一行就可以了

![ Max Square ](https://leetcode.com/media/original_images/221_Maximal_Square1.png?raw=true)

我们只需要前面的三个数据，相当于我们只需要两行，那么我们inplace的修改就只需要一行了，至于左上角的我们用一个特别变量表示就可以了。