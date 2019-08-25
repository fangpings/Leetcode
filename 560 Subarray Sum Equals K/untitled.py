from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        s = 0
        hashtable = defaultdict(int)
        for i in nums:
            s += i
            hashtable[s] += 1
        count = hashtable[k]
        s = 0
        for i in nums:
            s += i
            hashtable[s] -= 1
            count += hashtable[s+k]
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraySum([1,1,1], 2))
