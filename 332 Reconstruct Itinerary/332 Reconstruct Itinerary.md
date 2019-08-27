### 332 Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports `[from, to]`, reconstruct the itinerary in order. All of the tickets belong to a man who departs from `JFK`. Thus, the itinerary must begin with `JFK`.

**Note:**

1. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.
2. All airports are represented by three capital letters (IATA code).
3. You may assume all tickets form at least one valid itinerary.

**Example 1:**

```
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
```

**Example 2:**

```
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
```

### 想法

这个itinerary，我们可以这样考虑：有一个主路线，然后主路线的某些节点上有一些支线，**但是支线一定是一个环**（支线可以有很多个支线的支线，但是最后一定会回到主路线的节点上）。主路线可能是一个环或者一条线，但是由于我们选定是从JFK开始的，所以也不存在环的情况了。

于是我们可以利用DFS+Backtracking来做。

```python
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        hashtable = defaultdict(list)
        for dep, arr in sorted(tickets, reverse=True): #注意这里要反向，因为我们是倒着加进去的
            hashtable[dep].append(arr)
        ret = []
        def rec(dep):
            while hashtable[dep]:
                rec(hashtable[dep].pop())
            ret.append(dep)
        rec('JFK')
        return ret[::-1] #我们是倒着加进去的所以最后也要反向
        
```

整个顺序是这样的

```
targets = {'JFK': ['D', 'A'], 'A': ['C'], 'B': ['C'], 'C': ['JFK', 'D'], 'D': ['B', 'A']}
route = []
stack = ['JFK']
```

First point at which we get stuck:

```
targets = {'JFK': ['D'], 'A': [], 'B': ['C'], 'C': ['JFK', 'D'], 'D': ['B']}
route = []
stack = ['JFK', 'A', 'C', 'D', 'A']
```

Update route:

```
targets = {'JFK': ['D'], 'A': [], 'B': ['C'], 'C': ['JFK'], 'D': ['B']}
route = ['A']
stack = ['JFK', 'A', 'C', 'D']
```

Search forward again until stuck:

```
targets = {'JFK': [], 'A': [], 'B': [], 'C': [], 'D': []}
route = ['A']
stack = ['JFK', 'A', 'C', 'D', 'B', 'C', 'JFK', 'D']
```

Update route:

```
targets = {'JFK': ['D'], 'A': [], 'B': [], 'C': ['JFK'], 'D': []}
route = ['A', 'D', 'JFK', 'C', 'B', 'D', 'C', 'A', 'JFK']
stack = []
```

Return route in reverse:

```
route = ['JFK', 'A', 'C', 'D', 'B', 'C', 'JFK', 'D', 'A']
```

每次我们走到走不通（这个走不通的一定就是主线路的终点了），然后返回上一层，看看上一层能不能继续走（这就是通过递归实现的），如果可以走，那我们继续递归地走，在这个也走不通之后我们继续返回上一层。