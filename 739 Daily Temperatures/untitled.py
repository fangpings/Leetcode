class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in xrange(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

from collections import defaultdict
INT_MAX = 1000000

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temp = [0 for _ in range(101)]
        ret = [INT_MAX for _ in range(len(T))]
        for i in range(len(T) - 1, -1 , -1):
            for j in range(T[i] + 1, 101):
                if temp[j]:
                    ret[i] = min(ret[i], temp[j] - i)
            if ret[i] == INT_MAX:
                ret[i] = 0
            temp[T[i]] = i
        return ret