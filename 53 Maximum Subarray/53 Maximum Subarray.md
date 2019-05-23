### 53 Maximum Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Follow up:**

If you have figured out the O(*n*) solution, try coding another solution using the divide and conquer approach, which is more subtle.

### 想法

我觉得这题一点也不easy…果然是我的dp掌握的还是太差了

这题dp这么考虑，我们考虑$DP(i)​$是**以`nums[i]`结尾的subarray的最大值**,这样的话我们就有递推式
$$
DP(i)=
\begin{cases}
DP(i-1)+nums[i]& DP(i-1)>0\\
nums[i]& others
\end{cases}
$$
以及起始条件$DP(0)=nums[0]$

**以后遇到希望$O(N)$的算法用DP，特别是这种substring，subarray之类的，都可以考虑用包含当前位置的最xx来做DP，这样既保证了递推性，在最后选择的时候也只要取一下max就可以了**

考虑一下就可以知道，如果$DP(i-1)<0$那么$nums[i]$带上前面的肯定不划算，无论$nums[i]$的符号，如果$DP(i-1)>0$,由于我们要求$DP(i)$是以i结尾的subarray中最大的那一个，那么我们肯定要是$DP(i-1)+nums[i]$

最后我们取$max(DP)​$就可以了