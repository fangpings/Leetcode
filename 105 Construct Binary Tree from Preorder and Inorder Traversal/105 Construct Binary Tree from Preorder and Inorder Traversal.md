### 105 Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

**Note:**
You may assume that duplicates do not exist in the tree.

For example, given

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

Return the following binary tree:

```
    3
   / \
  9  20
    /  \
   15   7
```

#### 想法

1. 第一个办法比较慢一点，但是很好理解。`preorder[0]`一定是当前对应树的root。**然后我们在`inorder`中找到`preorder[0]`的index，在它左边的就是左子树(`inorder[:index]`)，在他右边的就是右子树(`inorder[index+1:]`)。**我们统计左子树和右子树分别的长度，然后在`preorder`中分别找到左子树对应的部分(`preorder[1:index+1]`)和右子树对应的部分(`preorder[index+1:]`), 因为inorder紧跟的是所有左子树的部分，然后是所有右子树的部分。我们有了左右子树对应的`inorder`和`preorder`数组，我们做递归就可以了。

2. 第一个方法比较慢的原因是找index需要O(N),然后再每个root也需要O(N),如果是最坏情况，即树退化成链表，那最坏情况就是O(N^2).第二个方法没有找index的环节。

   第二个方法是基于这么一个考虑的。我们不找`inorder`中的对应值，而是维护一个stop。**我们不断从左往右遍历`inorder`数组，左子树的stop是当前的rootvalue，而右子树的stop是上层的rootvalue**。`inorder`遍历到stop的时候，说明当前子树已经构建完毕了。如果是左子树构建完毕，那么从pop `inorder[0]`(左边的树全部都已经构建完毕，所以已经全部从`inorder`中去掉了)，然后继续构建右子树。

   构建的方法是`preorder[0]`作为rootvalue，然后pop掉，接下来rootvalue作为左子树的stopvalue递归构建左子树，上层的stopvalue作为右子树的stopvalue递归构建右子树。