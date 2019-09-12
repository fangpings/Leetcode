from collections import defaultdict

class Solution:
    def minTransfers(self, transactions):
        debts_map = defaultdict(int)
        for i, j, debt in transactions:
            debts_map[i] += debt
            debts_map[j] -= debt
        debts = []
        for _, debt in debts_map.items():
            if debt:
                debts.append(debt)
        return self.dfs(debts, 0, 0)

    def dfs(self, debts, pos, count):
        while pos < len(debts) and debts[pos] == 0:
            pos += 1
        if pos == len(debts):
            return count
        ret = 2**32
        for j in range(pos + 1, len(debts)):
            if debts[pos] * debts[j] < 0:
                debts[j] += debts[pos]
                ret = min(ret, self.dfs(debts, pos + 1, count + 1))
                debts[j] -= debts[pos]
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.minTransfers([[0,1,10], [2,0,5]]))