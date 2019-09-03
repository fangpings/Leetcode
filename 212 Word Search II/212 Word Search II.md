### 212 Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Example:**

```
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
```

**Note:**

1. All inputs are consist of lowercase letters `a-z`.
2. The values of `words` are distinct.

### 想法

对每个词构建trie树，然后对board里面的每个位置用bfs在trie树里搜索，直到当前的邻居全部不在trie当前节点中。注意不能重复，所以要用一个path来保存当前已经走过的位置。