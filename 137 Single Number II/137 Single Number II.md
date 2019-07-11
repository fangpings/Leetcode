### 137 Single Number II

Given a **non-empty** array of integers, every element appears *three* times except for one, which appears exactly once. Find that single one.

**Note:**

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1:**

```
Input: [2,2,3,2]
Output: 3
```

**Example 2:**

```
Input: [0,1,0,1,0,1,99]
Output: 99
```

### 想法

#### 抽象问题

给定一个数组，里面每个元素均出现了k次(`k > 1`)，除了一个元素出现p次(`p >= 1, p % k != 0`)。找到这个唯一的元素。

#### m-bit counter

首先我们来构建一个m-bit k-counter, 这个k-counter可以实现以下这个功能：对0,1数组进行count，每次遇到1的时候counter自增1，如果counter自增至k，则counter重新回到0

```python
counter = 0
for i in array:
		if i:
      	counter += 1
    if counter == k:
      	counter = 0
```

考虑什么位操作可以满足遇到0时不变,遇到1的时候自增，即自身取反（自增表示在碰到1的时候0会变成1而1会变成0）。很显然是`XOR`操作，即`1 ^ 1 = 0, 0 ^ 0 = 0, 0 ^ 1 = 1`。那我们就有了counter 的基本操作，即`counter  = counter ^ i`

但是简单自增只对1-bit的counter生效，而我们的k-counter至少要有m位，这里`m = [logk] + 1`。所以我们要对counter的每一位，考虑自增策略。对counter从高位到低位，我们以`c[m], c[m-1], c[m-2]...c[1]`来命名。那么`c[1]`的更新策略很简单，`c[1] = c[1] ^ i`。而对于第二位`c[2]`，当且仅当`i == 1 and c[1] == 1`时`c[2]`才应当进位，即`c[2] = c[2] ^ (c[1] & i)`。对于任意高位`c[k]`，进位条件应当是当且仅当`i == 1 and c[j] == 1 for all j < k`。

```python
for i in array:
  	c[m] ^= (c[m-1] & c[m-2] & ... & c[1] & i)
    ...
    c[2] ^= (c[1] & i)
    c[1] ^= i  # 注意要先从高位开始更新
```

这个时候我们的counter还不完善，它其实是个`2^m`-counter，而不是一个任意的k-counter。我们希望加入一个threshold，在counter达到threshold k的时候，自动跳变为0。于是我们可以使用一个mask，mask满足以下条件`mask = 0 if counter == k else 1 `。于是我们可以在每次更新时，对每一位都取mask，即`c[i] &= mask`。

那么我们的mask的更新策略是什么呢。假设k的二进制形式是`k[m], k[m-1], ..., k[1]`, 那么`mask = ~(y1 & y2 ... & ym) where yj = cj if kj = 1 else yj = ~ cj` 。这样子的话当`c == k`时，`yj`全部等于1，`mask`值为0，而 `c != k`时，`yj`必不全为1，则`mask`值必为1.

整体的更新策略如下

```python
for i in array:
  	c[m] ^= (c[m-1] & c[m-2] & ... & c[1] & i)
    ...
    c[2] ^= (c[1] & i)
    c[1] ^= i  # 注意要先从高位开始更新
    
    for j in range(m):
      	y[j] = c[j] if k[j] else ~c[j]
    mask = ~(y[1] & y[2] ... & y[m])
    
    for j in range(m):
      	c[m] &= mask
        ...
        c[1] &= mask
```

这样我们就得到了一个m-bit k-counter.

#### 32-bit integer counter

现在我们把注意力转向32-bit integer。我们从m-bit k-counter中得到的信息是，**如果`array`中1出现的次数正好为k，那么counter的值会为0**。另一点关键的信息是对于r-th bit而言，**所有a中非single的数的r-th bit之和一定为k的倍数，即对于一个m-bit k-counter，所有a中非single的数的r-th bit在这个counter中会被计数为0**.这一点启发了我们，我们希望问题中这些出现k次的元素最后不会影响counter的值。
$$
Sum(A_r) = k * m + p *Single_r
$$
则最后对于r-th bit而言，m-bit k-counter的最后的值为$p * Single_r$，这里$Single_r$表示只出现p次的数的r-th bit的值。于是我们有如下结论`counter_r = p if single_r = 1 else 0`, 这里`counter_r` 是m-bit k-counter。我们把`counter_r`和`p`均写成二进制的形式，则有`c_r[j] = p_r[j] if s_r = 1 else 0`。于是我们观察到，**对于`p_r[j] == 1`的那些`j`，我们有`c_r[j] = s_r`**。这一点是我们目前为止最重要的一个结论，这表明了我们的某些位置的counter的值实际上就等于我们在寻找的single元素的值。

剩下的事情就简单了。因为所有integer实际上是32-bit的（或者是16-bit，只要counter的位数和数组里面元素的位数一致即可）所以我们实际上可以维护m个32-bit counter，因为每一位实际上是独立的，所以32个m-bit k-counter实际上等同于m个32-bit k-counter。我们把这m个32位counter设置为`c[m], c[m-1],..., c[1]`, 于是最后我们只需要返回`c[j] if p[j] == 1`这样我们就结束了我们的工作。

#### 代码

回到本题，实际上这道题就是k=3, p=1，于是m=2，我们需要两个counter `x1`, `x2`

```python
c1 = 0
c2 = 0
m = 0
for i in nums:
  	c2 ^= c1 & i
    c1 ^= i
    mask = ~(c1 & c2) # k = 3, 二进制形式为11，则c1和c2都不用取反
    c1 &= mask
    c2 &= mask
return c1 # p = 1, 则最后c1 = single
```

