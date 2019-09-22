### 236 Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

**Example 1:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

**Example 2:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

**Note:**

- All of the nodes' values will be unique.
- p and q are different and both values will exist in the binary tree

### 想法

我们设置三个indicator: left, mid, right. 对于每个node，如果node本身等于p或q，那么我们设置mid=True。然后我们递归地搜索左子树和右子树，如果左子树找到了p或q，设置left=True，如果右子树找到了p或q，设置right=True

最后我们统计，如果三个indicator中有两个为True，那么这个node就是我们要找的了。（这肯定是最低的，比他再往上的节点不可能再有两个indicator指示为True，因为这个节点的返回值相当于把两个True变成一个True。(这里可以直接用bool值相加)

最后我们返回left or mid or right