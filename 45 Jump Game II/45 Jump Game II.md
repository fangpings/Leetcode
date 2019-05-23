### 45 Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

**Example:**

```
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Note:**

You can assume that you can always reach the last index.

### 想法

1. DP
   $$
   minjumps[i] = 
   \begin{cases}
   \inf& nums[i]=0\\
   1& nums[i]\geq l-1-i\\
   \min \limits_{j\leq \min(nums[i], l)-1}minjumps[j]+1& others
   \end{cases}
   $$
   DP的效率大概在$O(N^2)$，一个提高效率的方法是第三种情况我们从大往小找，当$minjumps[j]+1=2$的时候就停止搜索

2. BFS

   其实我没看出来是BFS，不过想法相当好，是一个$O(N)$的算法

   ```python
   def jump2(self, A):
       """
       Basically it's a shortest-path problem. 
       As an unweighted graph, BFS should be able to solve it in O(|E|).
       But as it's an array with non-negative numbers, we can't jump backward. 
       So we can do better here.
       Suppose we devided the arrays into segments depending on the elment 
       in the array. So for each segment, we find the farthest index we can 
       jump. For example, the first segment is always A[0]. The second will be
       from A[1] to A[A[0]]. The third will be from A[A[0]] to the farthest 
       index we can find in the second segment. We start looking between 
       the end of the last segment and the begin of the next segment.
       """
       ans = lastIdx = nextIdx = 0
       while nextIdx < len(A) - 1:
           ans += 1
           lastIdx, nextIdx = nextIdx, max(i + A[i] for i in xrange(lastIdx, nextIdx + 1))
       return ans
   ```

   我们考虑每走一步，能走到的最远的位置$d_k$，如果$d_k>len(nums)$，那么说明第$k$步就可以走到终点了。考虑第0步，能走的最远的位置和最近的位置都是`0`，第一步的起始位置是`1`，最远的位置是`A[0]`， 第二步能走到的最远距离是`max([i + A[i] for i in range(1, A[0] + 1)])`，即第一步的范围中能走到的最远的地方，而第二步的起始位置就是`A[0]`，这里的起始位置的意思是上一步中的最远位置，即**第k步起始位置之后的位置至少要通过k步才能走到**，而最远位置指的是**k步最远能走到的位置**。**要注意的是，k步范围内的所有位置，都可以在k步走到，因为对于所有k-1步的位置，若是在j处我们达到k步的最远位置，那么从j到k步最远位置中间肯定包括了k步的起始位置**