
from functools import reduce

class Solution:
    def canCompleteCircuit(self, gas, cost):
        total = 0
        index = 0
        current_sum = 0
        for i in range(len(gas)):
            current_sum += gas[i] - cost[i]
            if current_sum < 0:
                total += current_sum
                current_sum = 0
                index = i + 1
        total += current_sum
        return index if total >= 0 else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
            