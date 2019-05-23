### 91 Decode Ways

A message containing letters from `A-Z` is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Given a **non-empty** string containing only digits, determine the total number of ways to decode it.

**Example 1:**

```
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```

**Example 2:**

```
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

#### 想法

注意0是不进入编码的，单个的0是不行的。

主要是利用**DP**

```python
        for i in range(len(s) - 2, -1, -1):
            if s[i] != '0':
                if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]
```

主要是要判断一下2开头的时候行不行。dp数组的长度应当比s的长度再大1，然后dp[-1]=1，这样倒数第二位也能够正确解码。