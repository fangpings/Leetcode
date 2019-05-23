#### 31 Next Permutation

Implement **next permutation**, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be **in-place** and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

```
1,2,3` → `1,3,2`
`3,2,1` → `1,2,3`
`1,1,5` → `1,5,1
```

#### 想法

从最右边开始，找到升序排列的非降序序列，比如`[3,4,6,5,2,1]`的话就是`[6,5,2,1]`，这个自串没有改进空间了（相当于这个串的下一个要重排了），这个时候他的左边一位（这一位小于当前位）就是我们的改进目标，我们要在这个子串里找到**大于**那一位的最接近的位（在这个例子里面就是5），这个就是相当于进位之后的下一位，然后我们交换这两位的位置，对这个子串做升序排列再替换就可以了。