### 101 Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

 

But the following `[1,2,2,null,3,null,3]` is not:

```
    1
   / \
  2   2
   \   \
   3    3
```

 

**Note:**
Bonus points if you could solve it both recursively and iteratively.

#### 想法

首先，到了这题才发现前面用的`build_tree`函数错了。比如这个树`[5,4,1,null,1,null,4,2,null,2,null]`。4的左儿子是`null`，这意味着你在这个位置index乘2找到的不是这个null的左右儿子。即无脑index*2找左右儿子是不对的。修正的函数如下

```python
def build_tree(l):
    def rec(k):
        if k - 1 < len(l):
            if l[k-1]:
                node = TreeNode(l[k-1])
                node.left = rec(2*k)
                node.right = rec(2*k+1)
                return node
            else:
                l.insert(2*k-1, None)
                l.insert(2*k, None)
                return None
    return rec(1)
```

如果当前是null，那么在对应的2\*index和2*index+1的位置也插入null，防止index错乱。不知道有没有更好的做法。

然后回到这道题，一开始想的是用中序遍历成一个list，然后看看这个list是不是回文的，后来发现错了。`[5,4,1,null,1,null,4,2,null,2,null]`这个testcase就不对(这个testcase检测出了两个bug也是厉害)。

正确的做法是检查左右子树是不是相等，但是在检查之前，我们**把右子树的左右子树交换**。这样就可以了，就是这么简单。