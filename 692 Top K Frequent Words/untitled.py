import heapq
from collections import defaultdict
from functools import cmp_to_key

class Solution:
    def topKFrequent(self, words, k):
        hashmap = defaultdict(int)
        for w in words:
            hashmap[w] += 1
        tmp = []
        for key, item in hashmap.items():
            tmp.append((item, key))
        print(tmp)
        def cmp(x, y):
            if x[0] < y[0]:
                return -1
            elif x[0] > y[0]:
                return 1
            else:
                if x[1] < y[1]:
                    return 1
                elif x[1] > y[1]:
                    return -1
                else:
                    return 0
        return [x[1] for x in sorted(tmp, key=cmp_to_key(cmp), reverse=True)[:k]]
if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))