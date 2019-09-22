### 207 Course Schedule

There are a total of *n* courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, is it possible for you to finish all courses?

**Example 1:**

```
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```

**Example 2:**

```
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
```

**Note:**

1. The input prerequisites is a graph represented by **a list of edges**, not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).
2. You may assume that there are no duplicate edges in the input prerequisites.

### 想法

本质上就是找有向图里有没有环。

一个做法是用拓扑排序，每次找入度为0的节点，然后更新以这个节点出发到的节点的入度。

但是这个每次要重新找入度为0的节点太慢了。

另一个方法是用dfs找环，这里用的是dfs+backtracking。即我们用bfs做遍历，然后记录已经走过的node，在我们退出当前bfs深度之后，我们再把标记取消。

```python
def dfs(self, i, graph, visits):
    if visits[i] == -1:
    		return False
    if visits[i] == 1:
    		return True

    visits[i] = -1
    for req in graph[i]:
   		 if not self.dfs(req, graph, visits):
    			return False
    visits[i] = 1
    return True
```

这个写法很好啊，是一个典型的backtracking做法，可以好好学习一下