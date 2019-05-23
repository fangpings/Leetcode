### 89 Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer *n* representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

**Example 1:**

```
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
```

**Example 2:**

```
Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
```

#### 想法

事实上n位Gray码的后$2^{n-1}$位可以用前$2^{n-1}$位推出来。

```python
plus = 2 ** (n - 1)
second_half = [plus + x for x in first_half[::-1]]
```
然后n位Gray码的前$2^{n-1}$位实际上是和n-1位Gray码是一致的，所以我们直接递归计算就可以了。