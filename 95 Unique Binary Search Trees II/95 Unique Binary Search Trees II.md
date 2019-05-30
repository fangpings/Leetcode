### 95 Unique Binary Search Trees II

Given an integer *n*, generate all structurally unique **BST's** (binary search trees) that store values 1 ... *n*.

**Example:**

```
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

#### 想法

我们递归地生成子树。

首先我们遍历候选序列，从里面挑一个值作为根节点，然后对于小于根节点的值，我们将其作为新的候选序列，递归地生成**所有**左子树，同理，我们也生成所有的右子树，然后我们将所有左子树和右子树进行组合，就得到了当前序列的所有可能的二叉搜索树。