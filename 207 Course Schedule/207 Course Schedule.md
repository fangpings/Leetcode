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

一个方法是用dfs找环，这里用的是dfs+backtracking。即我们用dfs做遍历，然后记录已经走过的node，在我们退出当前bfs深度之后，我们再把标记取消。

```python
# visits 数组一开始设置为全0，visit为0表示该节点还未曾被访问过，visit为1表示该节点被访问过，且已确定从该节点出发并没有环（我们碰到这种节点可以直接确定当前路径上没有环，退出到上一层），visit为-1表示该节点在当前访问路径上（正在被判断是否有环），如果我们访问到了为-1的节点，说明我们在路径上碰到环了。
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

另一个方法是用bfs找环。

```python
for i in range(numCourses):
  	if inDegree[i] == 0:
    		queue.append(i)

    visited = []

    while queue:
      	preq = queue.pop()
      	visited.append(preq)
      	for course in hashMap[preq]:
        		inDegree[course] -= 1
        		if inDegree[course] == 0:
          			queue.append(course)
```

先找到所有入度为0的节点，加入队列，然后每次出队一个节点，更新他通往的所有节点，如果这些节点里面有任何入度为0的节点，加入队列（注意**新的入度为0的节点只会出现在这些节点中**）然后我们判断最后访问过的节点数和总节点数是否相等。