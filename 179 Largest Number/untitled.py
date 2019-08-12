class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if sum(nums) == 0:
            return '0'
        nums = [str(x) for x in nums]
        longest = len(max(nums, key=len))
        nums = sorted(nums, key=lambda x:x+x[0]*(longest-len(x)), reverse=True)
        return ''.join(nums)

if __name__ == '__main__':
    sol = Solution()
    print(sol.largestNumber([3,30,34,5,9]))