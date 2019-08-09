class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rec(left, right):
            if left == right:
                return left
            else:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    return rec(left, mid - 1)
                return rec(mid + 1, right)
        return rec(0, len(nums) - 1)

if __name__ == '__main__':
    sol = Solution()
    print(sol.findPeakElement([1,2,3,4,5,6,1]))