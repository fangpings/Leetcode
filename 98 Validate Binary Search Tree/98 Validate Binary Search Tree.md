### 98 Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than**the node's key.
- Both the left and right subtrees must also be binary search trees. 

**Example 1:**

```
    2
   / \
  1   3

Input: [2,1,3]
Output: true
```

**Example 2:**

```
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

#### 想法

继续递归地判断，只不过这次需要在每次调用的时候加上一个界。

每次调用递归函数的时候，首先判断`lower < node.val < upper`,然后对于左子树，bound变为`(lower, node.val)`,右子树则为`(node.val, upper)`。最开始的时候bound为`(-inf, inf)`