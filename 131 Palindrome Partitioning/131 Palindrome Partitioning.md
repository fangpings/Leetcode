### 131 Palindrome Partitioning

Given a string *s*, partition *s* such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of *s*.

**Example:**

```
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
```

#### 想法

简单的DP就行了，倒着找上来呗

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #dp[i] equal to the  all substring before i add the accroding dp[j]
        lens=len(s)
        if 0==lens:
            return [[]]
        dp=[[] for i in range(lens+1)]
        dp[-1]=[[]]
        for i in range(lens-1,-1,-1):
            for j in range(i+1,lens+1):
                if s[i:j]==s[i:j][::-1]:
                    for ele in dp[j]:
                        dp[i].append([s[i:j]]+ele)
        return dp[0]
```

我实在是太笨了