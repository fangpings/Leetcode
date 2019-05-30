### 99 Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

**Example 1:**

```
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
```

**Example 2:**

```
Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
```

**Follow up:**

- A solution using O(*n*) space is pretty straight forward.
- Could you devise a constant space solution?

#### 想法

我们考虑**中序遍历**。**中序遍历一棵二叉查找树我们最后将可以得到一个排序的数组**。所以我们的问题就转化为这个问题：一个排序数组的两个元素被交换了，怎么找到这两个元素？

考虑这个`1, 6, 3, 4, 5, 2`, 我们考虑当前元素和当前元素的前驱元素(考虑这两个元素也是因为中序遍历的时候找到这两个元素比较容易)。可以看到在第一个错误元素6的地方，有6 > 3，即6作为3的前驱元素出错。在第二个错误元素2的地方，5 > 2，2作为当前元素出错。即第一个出错位置，我们找前驱元素，第二个出错位置，我们找当前元素。

同时我们也需要考虑`1, 3, 2, 4`，如果是两个连续位置的数字交换，那么不存在第二个位置的错误元素了。所以我们在找到第一个错误位置之后，我们直接保存前驱元素和当前元素为两个出错位置，如果后面没有出错了，那直接交换这两个位置，如果后面没有出错，那么我们保存出错的当前位置为第二个出错位置。

回到这道题，**要求O(1)的空间复杂度意味着Stack或者递归都不能用了**。我们要用前面提到的Morris Traversal. Morris Traversal一个问题就是什么时候保存前驱元素不是很直观。如果我们递归地中序遍历，那么前驱元素的保存时机很明显，即

```
traverse(root.left)
predecessor = root
traverse(root.right)
```

在Morris Traversal里面，有两处可能的遍历地方。 但我们不用考虑这么多。只要每次遍历完当前元素之后（想象打印这个元素），我们直接保存`predecessor = root`就可以了。