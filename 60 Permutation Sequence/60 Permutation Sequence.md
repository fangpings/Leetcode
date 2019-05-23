### 60 Permutation Sequence

The set `[1,2,3,...,*n*]` contains a total of *n*! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for *n* = 3:

1. `"123"`
2. `"132"`
3. `"213"`
4. `"231"`
5. `"312"`
6. `"321"`

Given *n* and *k*, return the *k*th permutation sequence.

**Note:**

- Given *n* will be between 1 and 9 inclusive.
- Given *k* will be between 1 and *n*! inclusive.

**Example 1:**

```
Input: n = 3, k = 3
Output: "213"
```

**Example 2:**

```
Input: n = 4, k = 9
Output: "2314"
```

#### 想法

我们直接计算第'k'个位置应该是什么值。注意到，以`[1,2,3,4]`为例，`4123`是`4`开头的第一个，它的位置应该是`3*3！`，这启发我们可以像计算变动进制数一样去计算每一位的值，即首位应该是`(n-1)!`进制，次位应该是`(n-2)!`进制的。而该位的位数应该由k除以进制的余数来决定。我们**直接在待选数字中pop出余数index**即可。