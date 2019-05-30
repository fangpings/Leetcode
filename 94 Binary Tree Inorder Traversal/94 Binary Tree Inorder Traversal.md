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

#### Morris Traversal

**步骤：**

1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。

2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。

   a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。

   b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。输出当前节点。当前节点更新为当前节点的右孩子。

3. 重复以上1、2直到当前节点为空。

![img](https://images0.cnblogs.com/blog/300640/201306/14214057-7cc645706e7741e3b5ed62b320000354.jpg)

```python
# Python program to do inorder traversal without recursion and 
# without stack Morris inOrder Traversal 

# A binary tree node 
class Node: 
	
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# Iterative function for inorder tree traversal 
def MorrisTraversal(root): 
	
	# Set current to root of binary tree 
	current = root 
	
	while(current is not None): 
		
		if current.left is None: 
			print current.data, 
			current = current.right 
		else: 
			# Find the inorder predecessor of current 
			pre = current.left 
			while(pre.right is not None and pre.right != current): 
				pre = pre.right 

			# Make current as right child of its inorder predecessor 
			if(pre.right is None): 
				pre.right = current 
				current = current.left 
				
			# Revert the changes made in if part to restore the 
			# original tree i.e., fix the right child of predecessor 
			else: 
				pre.right = None
				print current.data, 
				current = current.right 

```

（要注意我们实际上是在实现**中序遍历**）左子树最右边的元素就是当前节点的前驱元素(predecessor)，这个元素的右子树肯定为NULL。如果左子树为NULL，那说明该节点已经没有前驱元素了(也就是说该元素是我们当前未打印元素中的最左元素)，我们直接打印这个元素就行。如果不为NULL，那我们找到前驱元素之后把他连接到当前元素(连在右子树上)，然后我们继续找左儿子的后继元素(successor)（实际上找前驱元素就是找到左子树最右边元素的后继元素），直到所有左边的元素都和其后继元素连接在一起(这个时候也一定是最左元素了)。然后我们开始按顺序打印。打印完当前节点之后会回到当前节点的右边，这个时候我们回到了当前元素的后继元素，这个元素我们已经遇到过了，但是我们还没有打印，这个时候再次寻找左子树的最右元素（当然这个时候我们不知道这个元素已经遇到过了，但是我们遇到过的话如果我们再进行找左子树的最右元素的操作，我们最后总是会回到现在的元素）（如果我们已经回到了后继元素，那么该元素的所有左边的元素都已经被打印过了），如果我们再进行找左子树的最右元素的操作，我们最后总是会回到现在的元素，这个时候我们就可以断开这个连接，恢复树本来的形状，然后我们再对当前元素的右子树进行相同的操作。

总的来说，这个操作就是先找到最左元素(中间会改变树的连接使得所有前驱都和它的后继正确地连接在一起)，然后回到它的后继，然后不断地找最左元素，改变连接使得后继正确地连接