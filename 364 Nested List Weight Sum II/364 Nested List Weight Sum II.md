### 364 Nested List Weight Sum II

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the [previous question](https://leetcode.com/problems/nested-list-weight-sum/) where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

**Example 1:**

```
Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.
```

**Example 2:**

```
Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
```

### 想法

一开始想的是比较笨的，先递归，统计最深的depth，然后用最深的depth减掉每个元素的depth作为每个元素最后的depth。

其实仔细一想，这个和一个字符串数字转换成int差不多，我们的做法是

```
num = 10 * num + str[k]
```

这里也差不多，我们用iterative的方法就类似于

```python
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        res, val = 0, 0
        while nestedList:
            next_level = []
            for item in nestedList:
                if item.isInteger():
                    val += item.getInteger()
                else:
                    next_level += item.getList()
            res += val
            nestedList = next_level
        return res
```

这里就是最外层循环是每个深度的循环，next_level就是表示下个深度的所有元素，而深度每加深一层，之前所有深度的所有元素就再被多加一次