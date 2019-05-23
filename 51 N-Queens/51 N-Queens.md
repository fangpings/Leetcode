### 51 N-Queens

The *n*-queens puzzle is the problem of placing *n* queens on an *n*×*n* chessboard such that no two queens attack each other.

![img](https://ws4.sinaimg.cn/large/006tNc79ly1g1xas2dq3hj307607o748.jpg)

Given an integer *n*, return all distinct solutions to the *n*-queens puzzle.

Each solution contains a distinct board configuration of the *n*-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space respectively.

**Example:**

```
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
```

### 想法

DFS+回溯，对于每行，尝试可能的所有位置，一旦判断某一行某个位置可行，继续搜索下一行的所有位置。

自己写的解法实在是太慢了，怀疑问题出在两个地方1. deepcopy占去太多时间，这是不必要的 2.对斜角的判断是用的搜索，实际上如果`(x, y)`已经在n-Queens里面了，那么对于位置`(p, q)`，如果`p + q = x + y`或者`p - q = x - y`，那么该位置处于`(x, y)`的斜线上，不可取。实际上我们只需要维护所有已加入n-Queens的**列位置，`x+y`，`x-y`**即可。

贴一个标准解法

```python
def solveNQueens(self, n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
    result = []
    DFS([],[],[])
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
```

