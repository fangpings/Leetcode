### 166  Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

**Example 1:**

```
Input: numerator = 1, denominator = 2
Output: "0.5"
```

**Example 2:**

```
Input: numerator = 2, denominator = 1
Output: "2"
```

**Example 3:**

```
Input: numerator = 2, denominator = 3
Output: "0.(6)"
```

### 想法

这道题还挺有意思的。主要问题在于要把循环部分找出来

首先一个小问题是要先把符号提出来，否则会影响计算。

其次我们考虑一下怎么才会循环，那只有某一位除法的余数在之前出现过的情况下才会出现循环了。所以我们记录每次除法的余数，直到该余数之前出现过或者余数等于0.还有一点注意的是不够除的话要不断对余数乘10，然后商要添0.