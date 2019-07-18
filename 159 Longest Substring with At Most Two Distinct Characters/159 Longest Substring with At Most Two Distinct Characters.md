### 159 Longest Substring with At Most Two Distinct Characters

Given a string **s** , find the length of the longest substring **t**  that contains **at most** 2 distinct characters.

**Example 1:**

```
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
```

**Example 2:**

```
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
```

### 想法

和字符串和数组相关的，第一个想到动态规划，第二个就应该想到sliding window。

其实这道题说破了用sliding window，剩下的就很trivial了。