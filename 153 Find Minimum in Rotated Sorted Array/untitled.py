class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                return nums[left]
        return min(nums[left], nums[right])

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin([1,2,3,4]))