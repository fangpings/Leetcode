### 94 Binary Tree Inorder Traversal

Given a binary tree, return the *inorder* traversal of its nodes' values.

**Example:**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

**Follow up:** Recursive solution is trivial, could you do it iteratively?

#### 想法

一切用递归的操作最后都可以用栈解决。

用两个while来模拟递归。里层while模拟左子树的搜索，外层while模拟右子树的搜索。