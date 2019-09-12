### 179 Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

**Example 1:**

```
Input: [10,2]
Output: "210"
```

**Example 2:**

```
Input: [3,30,34,5,9]
Output: "9534330"
```

**Note:** The result may be very large, so you need to return a string instead of an integer.

### 想法

先贴算法

```python
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
```

简单来说就是排序的key函数变成了x+y和y+x比较

现在我们来证明这样子是可行的，先把问题归纳一下

设$a_0,a_1,...,a_n$为非负整数,且满足对$\forall i, j$,若$i<j$,则a$_i\sim a_j > a_j\sim a_i$,其中$\sim$为拼接，即$12\sim34=1234$
证明$a_0\sim a_1 \sim ... \sim a_n$为所有可能的拼接中最大的.

证明：我们采用归纳法来证明。显然$a_0\sim a_1>a_1\sim a_0$成立

我们假设$a_0\sim a_1 \sim ... \sim a_n$是$n$个元素所有可能的拼接排列中最大的那一个。现在我们希望证明在加入$a_{n+1}$元素($a_{n+1}$小于$a_0,a_1,...,a_n$的拼接大小)后，$a_0\sim a_1 \sim ... \sim a_n \sim a_{n+1}$是$n+1$个元素所有可能的拼接排列中最大的那一个。

为此，我们定义一个交换操作。若相邻两个元素$a_i$和$a_j$满足$i>j$，则我们称一个交换操作为交换$a_i$和$a_j$的操作。显然，交换操作总是让整个拼接数变大。

如果我们随机固定剩下的$a_0,a_1,...,a_n$位置，然后随意插入$a_{n+1}$，我们发现由于剩下的数的下标总是小于$n+1$，所以我们总是可以通过交换操作将$a_{n+1}$换到序列的最后，也就是说若我们固定$a_0,a_1,...,a_n$位置，则将$a_{n+1}$插入到序列的最后是所有插入方法中最大的那一个。于是问题就变为了如何使$a_0,a_1,...,a_n$的拼接最大。由我们的假设条件，$a_0\sim a_1 \sim ... \sim a_n$是最大的情况，所以$a_0\sim a_1 \sim ... \sim a_n \sim a_{n+1}$为$n+1$个元素所有可能的拼接排列中最大的那一个。

