### 465 Optimal Account Balancing

A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as `[[0, 1, 10], [2, 0, 5]]`.

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

**Note:**

1. A transaction will be given as a tuple (x, y, z). Note that `x ≠ y` and `z > 0`.
2. Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.



**Example 1:**

```
Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
```



**Example 2:**

```
Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.
```

### 想法

我们先计算每个人的盈亏情况，得到一个数组balance

然后我们删掉balance里面所有为0的项，因为这个人和其他人没有金钱交易。

然后我们从头到尾一个一个把当前位置的人的盈亏变成0。这是怎么做到的呢，我们假设当前i位置的人的盈亏是b[i],那么我们从所有j>i的位置一个一个试（因为<i)的人的盈亏已经平衡了，不参与金钱交易），每当碰到b[j]和b[i]是异号的，我们就尝试着把b[i]的balance**直接加到**b[j]的头上，之后再去处理b[j]的帐。注意我们不知道怎么做才是optimal的，所以我们只能一个一个试验（DFS+backtracking）。

```python
        for j in range(pos + 1, len(debts)):
            if debts[pos] * debts[j] < 0:
                debts[j] += debts[pos]
                ret = min(ret, self.dfs(debts, pos + 1, count + 1))
                debts[j] -= debts[pos] # 注意试验完要恢复原样
```

