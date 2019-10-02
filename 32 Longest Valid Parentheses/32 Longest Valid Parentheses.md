### 32 Longest Valid Parentheses

Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

**Example 1:**

```
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
```

**Example 2:**

```
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
```

### 想法

我们可以这么看这个问题，当一个string是valid的时候，**当且仅当我们从左边看，它的左括号的个数永远大于等于右括号的个数，且最后左右括号个数相等，或者我们从右往左看，它的右括号的个数永远大于等于左括号的个数，且最后左右括号个数相等**。可能会有问题：第一个条件就已经充分了，为什么要第二个条件？这和我们的算法联系在一起。

从上面的想法我们很容易想到，我们从左往右走，用`left`和`right`统计左右括号的个数，当左括号等于右括号的时候我们记录当前子串长度，当右括号大于左括号的时候说明左边的子串已经不行了，更新起始位置到当前位置的下一位置。

那么一个问题就是有可能左括号的个数永远比右括号的个数多（因为整个串并不是valid的），例如`((()`，这种情况下我们就需要上面提到的第二个条件了，即我们从右往左再跑一遍，这样就不会漏掉了。

