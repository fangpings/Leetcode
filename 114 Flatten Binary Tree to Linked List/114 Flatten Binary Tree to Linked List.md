### 114 Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

```
    1
   / \
  2   5
 / \   \
3   4   6
```

The flattened tree should look like:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

#### 想法：

首先，之前的`build_tree`发现又写错了。。

```python
def build_tree(l):
    root = l.pop(0)
    if not root:
        return None
    root = TreeNode(root)
    nodes = [root]
    while l != []:
        left_val = l.pop(0)
        right_val = l.pop(0) if l != [] else None
        node = nodes.pop(0)
        if left_val:
            node.left = TreeNode(left_val)
            nodes.append(node.left)
        if right_val:
            node.right = TreeNode(right_val)
            nodes.append(node.right)
    return root
```

这次肯定没错了，这次改用queue来做，每次弹出`l`里面的两个元素作为当前节点的左右儿子，然后当前节点离开queue，两个儿子加入queue。

然后回到这道题，我们递归地整理左右子树，递归函数每次都返回右子树最后的元素，在函数里面我们先整理右子树，得到最右元素，然后我们整理左子树，得到左子树的最右元素，并通过这个元素将左子树和右子树拼接。最后我们返回右子树的最右元素，注意这里左右子树分别或同时为空的情况下返回值也会改变的。