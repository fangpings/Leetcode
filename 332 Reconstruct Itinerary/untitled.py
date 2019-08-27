from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        hashtable = defaultdict(list)
        for dep, arr in sorted(tickets, reverse=True):
            hashtable[dep].append(arr)
        ret = []
        def rec(dep):
            while hashtable[dep]:
                rec(hashtable[dep].pop())
            ret.append(dep)
        rec('JFK')
        return ret[::-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
