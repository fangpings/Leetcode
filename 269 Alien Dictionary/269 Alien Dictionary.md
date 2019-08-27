### 269 Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of **non-empty**words from the dictionary, where **words are sorted lexicographically by the rules of this new language**. Derive the order of letters in this language.

**Example 1:**

```
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
```

**Example 2:**

```
Input:
[
  "z",
  "x"
]

Output: "zx"
```

**Example 3:**

```
Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
```

**Note:**

1. You may assume all letters are in lowercase.
2. You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
3. If the order is invalid, return an empty string.
4. There may be multiple valid order of letters, return any one of them is fine.

### 想法

整个问题分成两步来做。第一步我们找出所有的前后依赖关系。这里我用的是Trie Tree。按照题目给出的顺序构建一棵Trie Tree，在每个节点都保存这个节点的儿子的字典顺序。因为我们是顺序插入的，所以我们插入的时候顺手就可以保存字典顺序。注意有些节点可能只有一个儿子，这个时候就不保存字典顺序了。Trie Tree的构建如下

```python
class Trie(object):
    def __init__(self):
        self.order = []
        self.children = {}

    def insert(self, s):
        if not s:
            return
        if s[0] not in self.children:
            self.children[s[0]] = Trie()
        if not self.order or self.order[-1] != s[0]: #这里是防止重复，注意只防止连续的重复，非连续的重复说明这个给出的顺序是无效的，会在后面处理
            self.order.append(s[0])
        self.children[s[0]].insert(s[1:]) #我们递归地去插入一个字符串

    def find_dependency(self):
        ret = []
        if len(self.order) > 1:
            ret.append(self.order) # 寻找整棵树的顺序依赖的时候我们只关注长度大于一的依赖关系（长度等于一就谈不上什么依赖了）
        for _, d in self.children.items():
            tmp = d.find_dependency()
            if tmp:
                ret += tmp
        return ret
```

构建完整个Trie树之后我们就可以得到我们想要的所有前后依赖关系了。接下来就可以进入第二步。**第二步是根据这些依赖关系（注意可能会有重复的依赖关系，这个时候一定要删掉，否则可能影响入度的计算）构建一个DAG即有向无环图，然后我们对这个图做拓扑排序，就可以得到我们想要的顺序。**根据依赖关系构建DAG实际上就是构建一个邻接表，邻接表我们用hashtable来做，每个item都是一个list。有了邻接表之后我们就来做拓扑排序，具体操作如下：在每一步统计所有节点的入度（即通向该节点的边数量），找到入度为0的节点，将它加入返回序列，然后把该节点出发的所有边的另一个顶点的入度减一。重复该操作，若在某一时刻还有未操作的节点，但是没有节点的入度为0了，说明这个图有环，我们不能找到一个拓扑排序。

最后注意一点，有些节点可能不会加入拓扑排序（例如输入`[['zx', 'zy']]`，这个时候`z`不会加入排序）所以最后我们要手动统计所有的字符，对于那些没有加入排序的字符，我们直接插入到最后（因为它们的顺序不影响）