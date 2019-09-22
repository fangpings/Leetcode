class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums += [0]
        l = len(nums)
        for n in nums:
            nums[n % l] += l
        ret = []
        for i, n in enumerate(nums):
            if n // l >= 2:
                ret.append(i)
        return ret
    