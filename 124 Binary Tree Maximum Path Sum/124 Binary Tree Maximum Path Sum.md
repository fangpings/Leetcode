### 124 Binary Tree Maximum Path Sum

Given a **non-empty** binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain **at least one node** and does not need to go through the root.

**Example 1:**

```
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
```

**Example 2:**

```
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```

#### 想法

我们递归地找。我们统计左右子树分别的最大Path Sum，再统计左右子树包含根节点的最大Path Sum，当前节点的最大Path Sum由`max(left_max, right_max, left_sum + right_sum + root.val)`来决定，而包含根节点的最大Path Sum则由`max(left_sum, right_sum) + root.val`决定。

注意要考虑负数的影响，左右子树包含root的最大Path Sum的最小值应当是0，这表示一个元素也不选

```python
class Solution:
    def maxPathSum(self, root):
        def rec(root):
            if not root:
                return -10000000, 0 #如果是None节点
            left_max, left_sum = rec(root.left)
            right_max, right_sum = rec(root.right)
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)
            return max(left_max, right_max, left_sum + right_sum + root.val), max(left_sum, right_sum) + root.val
        return rec(root)[0]
```

