### 145 Binary Tree Postorder Traversal

Given a binary tree, return the *postorder* traversal of its nodes' values.

**Example:**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
```

**Follow up:** Recursive solution is trivial, could you do it iteratively?

#### 想法

非递归的后续遍历是比较麻烦的一种。麻烦之处在于我们可能多次碰到某一元素，第一次碰到的时候是我们把该元素加入到栈的时候，这个时候不需要做什么特别的操作。但是我们在遍历完他的左子树之后（也就是把栈里面他的左子树的元素pop完之后），**我们就遇到问题了：现在栈顶还是这个元素，但我们怎么知道这是左子树遍历结束之后，还是右子树遍历结束之后呢？如果是前者，我们应该继续遍历右子树，如果是后者，我们应该把这个元素出栈。**

所以答案就是我们在单纯给节点入栈的时候，应该同时记录元素现在的状态（左右子树均未遍历，左子树已遍历，左右子树均已遍历）。

每次循坏，我们检查栈顶元素，根据栈顶元素状态来决定我们接下来的行动。