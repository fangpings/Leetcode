class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 2 and i < r:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            elif nums[i] == 0 and i >= l:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            else:
                i += 1


if __name__ == '__main__':
    sol = Solution()
    a = [0,1,2,0,1,2]
    sol.sortColors(a)
    print(a)
