### 654 Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

1. The root is the maximum number in the array. 
2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

**Example 1:**

```
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
```

**Note:**

1. The size of the given array will be in the range [1,1000].

### 想法

O(N^2)的算法是trivial的，递归生成，每次找subgroup里的最大值就可以了。

但是还有一个极强的O(N)做法

![1](/Users/Kururuken/Desktop/Leetcode/654 Maximum Binary Tree/1.jpeg)

我们顺序地插入数组里的每一个元素。注意每次插入的时候，都只会沿着当前树的右边走，因为左边是属于当前节点的左边元素的，我们不可能再去干涉了。那么走到什么时候停，停下来的时候又做什么呢？我们一路沿右边走，走到当当前节点的元素小于我们需要插入的元素的时候就可以停下了。这个时候我们把当前元素当做我们的左儿子（因为要求是左儿子是在[上一个比当前元素大的元素(直接父亲), 当前元素]这个区间中最大的元素，那就是我们一路弹出的最后一个元素（因为他本来是上一个比当前元素大的元素的右儿子，说明他之前是这个区间的老大，现在我们取代了他的位置，我们变成了这个区间的老大，然后这个元素又在我们的左边，所以这个元素成了我们左边到上一个比我们大的元素之间的区间的老大。然后上一个比我们大的元素就是我们的父亲节点。看上图，我们发现一个栈的结构就可以搞定这件事情了。