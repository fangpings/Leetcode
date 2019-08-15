### 199 Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the *right* side of it, return the values of the nodes you can see ordered from top to bottom.

**Example:**

```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

### 想法

1. 层序遍历，找出每一层的所有元素（用queue），然后标记最右边的元素即可（因为queue的元素是有顺序的进出的）
2. DFS。在DFS的时候记得同时要保存两个深度信息，一个是当前已经发现最右元素的最深深度，另一个是当前DFS搜索的深度，如果当前DFS搜索的深度大于当前已经发现的最右元素的最深深度，那么把当前元素加入最右元素列表。搜索的时候要先搜索右边的元素