### 1048 Longest String Chain

Given a list of words, each word consists of English lowercase letters.

Let's say `word1` is a predecessor of `word2` if and only if we can add exactly one letter anywhere in `word1` to make it equal to `word2`.  For example, `"abc"` is a predecessor of `"abac"`.

A *word chain* is a sequence of words `[word_1, word_2, ..., word_k]` with `k >= 1`, where `word_1` is a predecessor of `word_2`, `word_2` is a predecessor of `word_3`, and so on.

Return the longest possible length of a word chain with words chosen from the given list of `words`.

**Example 1:**

```
Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
```

**Note:**

1. `1 <= words.length <= 1000`
2. `1 <= words[i].length <= 16`
3. `words[i]` only consists of English lowercase letters.

### 想法

先把原来的数组按字符串长度从小到大排序，把每个字符串都存进dict，value是字符串在数组中的位置。然后我们开始用DP，对于每个字符串，我们对于每个可能的chain的上一环节`tmp = st[:j]+st[j+1:]`，都在dict里寻找是否存在，如果存在，那么`dp[i] = max(dp[i], dp[dic[tmp]] + 1)`

