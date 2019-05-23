class Solution:
    def removeDuplicates(self, nums):
        l = len(nums)
        i = 0
        while i < l:
            if i + 1 < l and nums[i] == nums[i+1]:
                i += 1
                while i + 1 < l and nums[i+1] == nums[i]:
                    l -= 1
                    nums.remove(nums[i])
            i += 1
        return len(nums)

if __name__ == '__main__':
    sol = Solution()
    array = [1,2,3]
    ret = sol.removeDuplicates(array)
    print(array, ret)