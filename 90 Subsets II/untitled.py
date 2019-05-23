class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ret = []
        def select_k(nums, k):
            if k == 0:
                return [[]]
            if k == 1:
                ret = []
                i = 0
                l = len(nums)
                while i < l:
                    ret.append([nums[i]])
                    while i + 1 < l and nums[i] == nums[i+1]:
                        i += 1
                    i += 1
                return ret
            ret = []
            i = 0
            while i <= len(nums) - k:
                ret += [[nums[i]] + x for x in select_k(nums[i + 1:], k - 1)]
                while i + 1 <= len(nums) - k and nums[i] == nums[i+1]:
                    i += 1
                i += 1
            return ret

        for k in range(len(nums) + 1):
            ret += select_k(nums, k)
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsetsWithDup([4,4,4,1,4]))