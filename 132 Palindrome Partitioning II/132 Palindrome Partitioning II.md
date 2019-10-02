### 132 Palindrome Partitioning II

Given a string *s*, partition *s* such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of *s*.

**Example:**

```
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

### 想法

`dp[j]`表示从j位置到数组最后的最小cut数。于是有如下更新

```
dp[j] = min(dp[i] + 1) if s[j:i+1] is palindrome
```

需要注意的是，如果`s[j:]`是回文的，那么`dp[j] = 0`，即我们如果我们循环到`i = l - 1`，我们需要特别判断一下。

至于对于任意`i, j`，如何判断`s[j:i+1]`是否为回文，我们需要记录`s[j+1:i]`是否为回文，即`isPalindrome[j][i] = isPalindrome[j+1][i-1] and s[j] == s[i]`，同样要注意`j = i` 和`j = i - 1`的base case的处理