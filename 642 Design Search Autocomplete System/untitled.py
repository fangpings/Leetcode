from collections import defaultdict
from functools import cmp_to_key

class Trie(object):
    def __init__(self):
        self.sentences = set()
        self.next = {}

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = Trie()
        self.current_node = self.root
        self.current_sentence = ''
        self.freq = defaultdict(int)
        for sentence, time in zip(sentences, times):
            self.freq[sentence] = time
            self.insert(sentence)

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self.freq[self.current_sentence] += 1
            self.insert(self.current_sentence)
            self.current_node = self.root
            self.current_sentence = ''
        else:
            if not self.current_node:
                self.current_sentence += c
                return []
            elif c not in self.current_node.next:
                self.current_sentence += c
                self.current_node = None
                return []
            else:
                self.current_node = self.current_node.next[c]
                self.current_sentence += c
                return sorted(self.current_node.sentences, key=cmp_to_key(self.cmp), reverse=True)[:3]

    def cmp(self, a, b):
        if self.freq[a] > self.freq[b]:
            return 1
        elif self.freq[a] < self.freq[b]:
            return -1
        else:
            if a > b:
                return -1
            else:
                return 1

    def insert(self, s):
        node = self.root
        for c in s:
            if c not in node.next:
                node.next[c] = Trie()
            node = node.next[c]
            node.sentences.add(s)



# ["AutocompleteSystem","input","input","input","input","input","input","input","input","input","input","input","input"]
# [[["i love you","island","iroman","i love leetcode"],[5,3,2,2]],["i"],[" "],["a"],["#"],["i"],[" "],["a"],["#"],["i"],[" "],["a"],["#"]]

if __name__ == '__main__':
    sol = AutocompleteSystem(["i love you","island","iroman","i love leetcode"],[5,3,2,2])
    print(sol.input('i'))
    print(sol.input(' '))
    print(sol.input('a'))
    print(sol.input('#'))
    print(sol.input('i'))
    print(sol.input(' '))
    print(sol.input('a'))
    print(sol.input('#'))
    print(sol.input('i'))
    print(sol.input(' '))
    print(sol.input('a'))
    print(sol.input('#'))