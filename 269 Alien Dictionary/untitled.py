from collections import defaultdict
class Trie(object):
    def __init__(self):
        self.order = []
        self.children = {}

    def insert(self, s):
        if not s:
            return
        if s[0] not in self.children:
            self.children[s[0]] = Trie()
        if not self.order or self.order[-1] != s[0]:
            self.order.append(s[0])
        self.children[s[0]].insert(s[1:])

    def find_dependency(self):
        ret = []
        if len(self.order) > 1:
            ret.append(self.order)
        for _, d in self.children.items():
            tmp = d.find_dependency()
            if tmp:
                ret += tmp
        return ret


class Solution:
    def alienOrder(self, words):
        if not words:
            return ''
        root = Trie()
        for w in words:
            root.insert(w)
        dependency = root.find_dependency()
        new_dependency = set()
        for d in dependency:
            for i in range(len(d) - 1):
                new_dependency.add((d[i], d[i+1]))
        adjacency = defaultdict(list)
        for pair in new_dependency:
            adjacency[pair[0]].append(pair[1])
        indgree = defaultdict(int)
        for k, l in adjacency.items():
            if k not in indgree:
                indgree[k] = 0
            for c in l:
                indgree[c] += 1
        ret = ''
        while indgree:
            min_in = self.findmin(indgree)
            if not min_in:
                return ''
            ret += min_in
            for c in adjacency[min_in]:
                indgree[c] -= 1
        new_set = set()
        for c in ret:
            new_set.add(c)
        for w in words:
            for c in w:
                if c not in new_set:
                    new_set.add(c)
                    ret += c
        return ret

    def findmin(self, indgree):
        for k, i in indgree.items():
            if i == 0:
                indgree.pop(k)
                return k
        return None

if __name__ == '__main__':
    sol = Solution()
    dic = [
    'z',
    'z'
]
    print(sol.alienOrder(dic))

