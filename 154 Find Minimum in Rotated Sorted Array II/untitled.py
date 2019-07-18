class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high - 1:
            while low < high - 1 and nums[low] == nums[high]:
                low += 1
            mid = (low + high) // 2
            if nums[low] <= nums[mid] and nums[mid] <= nums[high]:
                return nums[low]
            elif nums[low] > nums[mid]:
                high = mid
            else:
                low = mid
        return min(nums[low], nums[high])

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin([3,3,1,3]) == 1)
    print(sol.findMin([3,3,3,3,3,3,1,2,3]) == 1)
    print(sol.findMin([1]) == 1)
    print(sol.findMin([1,2]) == 1)
    print(sol.findMin([2,1]) == 1)
    print(sol.findMin([1,2,3]) == 1)
    print(sol.findMin([2,3,1]) == 1)
    print(sol.findMin([3,1,2]) == 1)
    print(sol.findMin([1,2,3,4]) == 1)
    print(sol.findMin([4,1,2,3]) == 1)
    print(sol.findMin([3,4,1,2]) == 1)
    print(sol.findMin([2,3,4,1]) == 1)
    print(sol.findMin([1,1]) == 1)
    print(sol.findMin([1,1,1]) == 1)
    print(sol.findMin([1,1,1,1]) == 1)
    print(sol.findMin([1,1,2]) == 1)
    print(sol.findMin([1,2,1]) == 1)
    print(sol.findMin([2,1,1]) == 1)
    print(sol.findMin([1,1,1,2]) == 1)
    print(sol.findMin([1,1,2,1]) == 1)
    print(sol.findMin([1,2,1,1]) == 1)
    print(sol.findMin([2,1,1,1]) == 1)
    print(sol.findMin([1]) == 1)
