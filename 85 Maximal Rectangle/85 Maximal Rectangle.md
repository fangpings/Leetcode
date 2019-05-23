### 85 Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

**Example:**

```
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```

#### 想法

我真的是傻了。。

记录一个`heights`数组，初始为全0，然后遍历matrix的每一层，如果这一层的`i`位置标记为`1`，则`heights[i] +=1`，否则置零，这样我们就得到一个到第`k`层的histogram，然后我们再用找histogram里面最大的长方形的算法，找到到每一层为止的最大长方形，然后就可以找到整个matrix里面最大的长方形了。