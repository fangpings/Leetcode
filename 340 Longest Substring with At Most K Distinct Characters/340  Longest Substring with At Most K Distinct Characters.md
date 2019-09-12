### 340  Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most *k*distinct characters.

**Example 1:**

```
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
```

**Example 2:**

```
Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
```

### 想法

标准的Sliding Window做法，在sliding window里面维护一个hashmap来记录相同字符的出现次数，再在外面维护一个不同字符的出现次数就行。