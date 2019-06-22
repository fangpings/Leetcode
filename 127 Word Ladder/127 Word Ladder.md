### 127 Word Ladder

Given two words (*beginWord* and *endWord*), and a dictionary's word list, find the length of shortest transformation sequence from *beginWord* to *endWord*, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list. Note that *beginWord*is *not* a transformed word.

**Note:**

- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume *beginWord* and *endWord* are non-empty and are not the same.

**Example 1:**

```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
```

**Example 2:**

```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```

### 想法

#### 总体

本质上这是个图论问题。无向图的最短路径，应该用BFS解决（这里也用不着用Dijkstra，Dijkstra算法是求出单个顶点到其他所有顶点的最短路径的算法，求出某个顶点到另一个顶点的最短路径算法只需要BFS就可以了）

![graph](/Users/Kururuken/Desktop/Leetcode/127 Word Ladder/graph.jpg)

#### BFS和DFS

一开始居然写成了DFS。。不过就顺便复习一下DFS好了

DFS是用栈的，当然也可以用递归，这样就省的自己去保存状态了。如果要自己保存状态的话，要另外再多存一个数据结构保存

```python
stack = [beginWord]
min_steps = 1000000
recorder = defaultdict(int)  #记录每个元素的进度，每当该元素出栈之后就会重置
while stack:
    current = stack[-1]  #栈顶为当前元素
    if recorder[current] < len(next_map[current]):
        next_word = next_map[current][recorder[current]]  #已经保存的邻接元素
        if next_word not in stack:  #防止重复
            if next_word == endWord:
                if len(stack) + 1 < min_steps:
                    min_steps = len(stack) + 1
                stack.pop()  #结束搜索，当前元素出栈
                recorder[current] = 0  #重置进度
            else:
                stack.append(next_word)  #继续搜索
                recorder[current] += 1  #进度+1
        else:
            recorder[current] += 1
    else:
        recorder[current] = 0
        stack.pop()
return 0
```

当然这道题用DFS是完全错误的。。应当用BFS。BFS用Queue来进行，每次队列最后的元素出队，然后和这个元素邻接的元素全部进栈，**一旦我目标元素进队列了，我们就可以直接返回深度了（这里不存在后面还会有更短的路径这种情况了，因为队列相当于树的层序了，你在某一层碰到了目标元素，后面即使再碰到，层数也只会加深，所以一旦碰到了肯定就是最短路径）**

BFS反而更好写一点，都不用保存状态，注意要保存一下已经访问的节点就可以了，**已经访问过的节点在后面永远不需要访问了**。

```python
queue = [(beginWord, 1)]
visited = []
while queue:
    current, steps = queue.pop(0)
    for i in range(len(beginWord)):
        for next_word in all_combo_dict[current[:i] + '*' + current[i+1:]]:  #这个就相当于是邻接元素了
            if next_word == endWord:
                return steps + 1
            if next_word not in visited:
                queue.append((next_word, steps + 1))
                visited.append(next_word)
        all_combo_dict[current[:i] + '*' + current[i+1:]] = []
return 0
```

#### 邻接矩阵

这个是这道题特有的。一般图论要知道顶点的邻接关系总需要一个邻接矩阵，不过建立邻接矩阵这个操作本身就是O(N^2)了。这道题判断是否邻接也很麻烦。

这里有两个办法，一个是预先建立一个表，对于在wordlist的里面的每个词的每个位置都用\*去替换，在BFS的时候一旦遇到某个词，也把它的每个位置用\*去替换，然后在表里面找

```python
for word in wordList:
		for i in range(len(beginWord)):
				all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)  # 形如h*t的wordlist中的邻接元素
```

另一个方法是直接对word的每个位置用a-z去替换，然后看替换完的词在不在wordlist里面。

#### 双向BFS

**我们同时对起点和终点进行BFS，如果起点的搜索和终点的搜索在某一步有了相同的元素，那说明就找到了一条从起点通往终点的路径。**这样做可以把搜索的空间减小一半。

#### 优化

**用set好像可以加快不少**。以前没怎么用过这个数据结构。

*python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.*

*sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作。*

别人的飞快代码，学习一下

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        begin = set([beginWord])
        end = set([endWord])
        words = set(wordList)
        if endWord not in words:
            return 0
        dis = 1
        while begin and end:
            if len(begin) > len(end):  # 双向BFS，每次对begin和end中较短的那个做BFS
                begin, end = end, begin
            temp = set()  #这里直接建立下一层的集合
            for word in begin:
                for i, c in enumerate(word):
                    left, right = word[:i], word[i + 1:]
                    for char in 'abcdefghijklmnopqrstuvwxyz':  #直接用26个字母去替换所有可能位置去试
                        next_word = left + char + right
                        if next_word in end:  #如果下一步的可能元素在另一个集合里面，结束搜索
                            return dis + 1
                        if next_word in words:
                            words.discard(next_word)  #删掉已经有的元素防止重复
                            temp.add(next_word)
            begin = temp
            dis += 1
        
        return 0
```

