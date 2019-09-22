### 426 Convert Binary Search Tree to Sorted Doubly Linked List

Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:

![img](https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png)

We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

![img](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)

Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

![img](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturnbst.png)

### 想法

每次递归，我们返回该节点最左边的节点和最右边的节点。然后对于每个节点，我们对左子树和右子树分别做这个，然后我们把左子树的最右边接到节点左边，再把右子树的最左边接到节点的右边。（注意左右子树完成递归之后他们已经是链表的形式了）