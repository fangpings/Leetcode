### 161 One Edit Distance

Given two strings **s** and **t**, determine if they are both one edit distance apart.

**Note:** 

There are 3 possiblities to satisify one edit distance apart:

1. Insert a character into **s** to get **t**
2. Delete a character from **s** to get **t**
3. Replace a character of **s** to get **t**

**Example 1:**

```
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
```

**Example 2:**

```
Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
```

**Example 3:**

```
Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
```

### 想法

和72 Min Edit Distance的时候肯定不一样了。再用DP肯定很慢。

Edit Distance为1的情况肯定只有两个字符串长度相同或者相差1的情况。如果字符串长度相同，我们遍历两个字符串，当且仅当有一个字符不同时Edit Distance才为1。如果两个字符串长度相差1，我们同时开始遍历两个字符串，当碰到第一个不同的字符的时候，我们把**较长的字符串的指针后移一位，但是较短的字符串的指针不动，然后继续开始遍历，此时如果再有一个字符不匹配，那么就Edit Distance就不是1了**。