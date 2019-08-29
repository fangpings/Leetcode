class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_counts = 0
        if not nums:
            return
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_counts += 1
            else:
                nums[i-zero_counts] = nums[i]
        for i in range(-1, -1-zero_counts, -1):
            nums[i] = 0
            