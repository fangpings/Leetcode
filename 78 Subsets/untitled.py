class Solution:
    def subsets(self, nums):
        ret = []
        def select_k(nums, k):
            if k == 0:
                return [[]]
            if k == 1:
                return [[i] for i in nums]
            ret = []
            for i in range(len(nums) - k + 1):
                ret += [[nums[i]] + x for x in select_k(nums[i + 1:], k - 1)]
            return ret

        for k in range(len(nums) + 1):
            ret += select_k(nums, k)
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1]))



