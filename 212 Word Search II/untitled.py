def ch(c):
    return ord(c) - ord('a')

class Trie(object):
    def __init__(self):
        self.word = ''
        self.next = [None for _ in range(26)]
        self.chs = set()

    def insert(self, word, idx):
        if idx == len(word):
            self.word = word
        else:
            self.chs.add(word[idx])
            if not self.next[ch(word[idx])]:
                self.next[ch(word[idx])] = Trie()
            self.next[ch(word[idx])].insert(word, idx+1)

class Solution:
    def findWords(self, board, words):
        self.m = len(board)
        if not self.m:
            return []
        self.n = len(board[0])
        if not self.n:
            return []

        self.board = board
        self.root = Trie()
        for word in words:
            self.root.insert(word, 0)

        self.ret = set()
        self.words = set(words)
        self.path = set()
        for i in range(self.m):
            for j in range(self.n):
                self.search(self.root.next[ch(self.board[i][j])], i, j)
        return list(self.ret)

    def search(self, node, i, j):
        if node and (i, j) not in self.path:
            if node.word:
                self.ret.add(node.word)
            self.path.add((i, j))
            # print(self.path)
            # print(i, j, node.chs, self.path, node.next)
            if i > 0:
                # if self.board[i-1][j] in node.chs:
                #     print(self.board[i-1][j], ch(self.board[i-1][j]))
                self.search(node.next[ch(self.board[i-1][j])], i - 1, j)
            if i < self.m - 1:
                # if self.board[i+1][j] in node.chs:
                #     print(self.board[i+1][j], ch(self.board[i+1][j]))
                self.search(node.next[ch(self.board[i+1][j])], i + 1, j)
            if j > 0:
                # if self.board[i][j-1] in node.chs:
                #     print(self.board[i][j-1], ch(self.board[i][j-1]))
                self.search(node.next[ch(self.board[i][j-1])], i, j - 1)
            if j < self.n - 1:
                # if self.board[i][j+1] in node.chs:
                #     print(self.board[i][j+1], ch(self.board[i][j+1]))
                self.search(node.next[ch(self.board[i][j+1])], i, j + 1)
            self.path.discard((i, j))

if __name__ == '__main__':
    sol = Solution()
    board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
    words = ["oath","pea","eat","rain"]
    print(sol.findWords(board, words))





