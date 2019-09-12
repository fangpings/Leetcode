### 222 Count Complete Tree Nodes

Given a **complete** binary tree, count the number of nodes.

**Note:** 

**Definition of a complete binary tree from Wikipedia:**
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

**Example:**

```
Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
```

### 想法

先找到层数，事实上我们只关心最后一层有几个node。再注意到一点，那就是如果最后一层超过一半，那根节点左子树应该是满树（也就是左子树一直往右走是走得到头的），这就提醒我们**可以用二分查找去做了**。每次我们都在当前节点的左儿子一路往右走，如果最后能走到底层，那么我们加上对应的最底层个数，然后我们的下个节点选右儿子，否则我们什么都不加，下个节点选左儿子。我们每次下降一层，就可以减少一半，于是我们的时间复杂度就提升到O(log^2N)