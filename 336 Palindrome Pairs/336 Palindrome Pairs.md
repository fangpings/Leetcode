### 336 Palindrome Pairs

Given a list of **unique** words, find all pairs of **distinct** indices `(i, j)` in the given list, so that the concatenation of the two words, i.e. `words[i] + words[j]` is a palindrome.

**Example 1:**

```
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
```

**Example 2:**

```
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
```

### 想法

两个词w1(`len(w1) = i`)和w2(`len(w2) = j`)拼起来能构成回文，那只有以下这些情况

1. `i < j and w1[::-1] == w2[:i] and w2[i:] == w2[i:][::-1]`，这个时候`w2~w1`为回文。w1插在w2后面，w1和w2前半部分（与w1等长）构成回文，w2剩下的部分自己构成回文
2. `i < j and w1[::-1] == w2[-i:] and w2[:-i] == w2[:-i][::-1]`，这个时候`w1~w2`为回文，w1插在w2前面。
3. `i > j`的同样两种情况

那么我们可以对每个词的每个位置做分割，然后对每个分割，前半部分reverse之后找有没有相同的字符串，后半部分与自己的回文做对比，如果都满足，那么表示这两个可以构成一个拼接回文。同理再对后半部分reverse找相同。

因为要找有没有相同字符串，并且还要得到index，所以我们很自然地考虑用hashtable就可以了。时间复杂度应该在O(NK^2),只需要遍历两边所有字符串，所以是O(N)，对每个字符串的每个位置都要判断回文，所以是O(K^2)

千万不要用trie tree，难写对还效率不见得高。