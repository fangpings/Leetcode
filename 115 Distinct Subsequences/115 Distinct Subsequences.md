### 115 Distinct Subsequences

Given a string **S** and a string **T**, count the number of distinct subsequences of **S** which equals **T**.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, `"ACE"` is a subsequence of `"ABCDE"` while `"AEC"` is not).

**Example 1:**

```
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
```

**Example 2:**

```
Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
```

#### 想法

动态规划。`DP[j][i]`表示`S[:i+1]`中的subsequence和`T[:j+1]`一致的数量。最后我们要return的是`DP[-1][-1]`。

首先我们初始化`DP[0][0]`, `dp[0][0] = 0 if s[0] != t[0] else 1`这个很显然。如果`S`和`T`的首位相等就是1，否则是0.

然后我们初始化`DP`矩阵的第一行。`dp[0][i] = dp[0][i-1] + 1 if s[i] == t[0] else dp[0][i-1]`。注意到如果`S`的第`i`位和`T[0]`一致，那么所有`>i`位置作为终点的串，至少都会有`i`位置这个subsequence，所以`DP`的每一行都是递增数列。当`i`位置上两字符串一致的时候，我们在`i-1`位置的基础上再+1

然后我们初始化剩下的行，`dp[j][i] = dp[j][i-1] + dp[j-1][i-1] if s[i] == t[j] else dp[j][i-1]`。我们以`bagbag`和`bag`来说明

```
[1, 1, 1, 2, 2, 2]
[0, 1, 1, 1, *3*, 3]
[0, 0, 1, 1, 1, 4]
```

我们看打星号的位置。这个位置是`bagba`和`ba`重合的地方，因为两个串的`a`都一致，所以我们肯定要更新。因为寻找上一位一致的子串，也就是`b`的时候，在`S`的这个位置**之前的一个位置**（因为实际上这个位置要留给`a`去重合）我们有两个重合子串，所以这个位置`a`一致意味着`S`以这个位置为终点的地方将会有两个重合子串，也就是`dp[j-1][i-1]`部分。我们还有第二部分也就是前面已经找到的一个重合子串，我们把两部分加起来就得到最后的结果。复杂度O(MN)

不过这个比较慢，看一个飞快的

```python
from collections import defaultdict

class Solution:
    
    def numDistinct(self, s: str, t: str) -> int:

        # To begin, we build up an index for t that allows
        # us to quickly access all of the locations of a 
        # particular character.
        index_for_t = defaultdict(list)
        for index, letter in enumerate(t):
            index_for_t[letter].append(index)
        
        # And now we use dynamic programming to iterate 
        # through string s, keeping track of all the 
        # partial and complete solutions we've seen.
        # I further explain the trick here below.
        dp_array = [0] * (len(t) + 1)
        dp_array[0] = 1
        for character in s:
            for index in reversed(index_for_t[character]):
                dp_array[index + 1] += dp_array[index]
        
        # The solution will now be in the final dp array slot.
        return dp_array[-1]
```

只遍历一次`S`，`dp[j+1]`储存`j`位置`T[:j+1]`一致的`S`的子串。每次在`S`中碰到`T`中已经有的字符，意味着这个字符对应的index的`dp`slot可以加上所有`index-1`位置的重合子串，因为index-1位置子串重合数量有了，再加上这个index在`S`中也对应了，则我们可以加上这些数量的子串。时间复杂度为O(M+N)(大致上)（这个新的方法我实在看不懂啊。。。）