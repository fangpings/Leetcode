class Solution:
    def search(self, nums, target):
        if not nums:
            return False

        low, high = 0, len(nums) - 1

        while low <= high:
            while low < high and nums[low] == nums[high]:
                low += 1
            mid = (low + high) // 2
            if target == nums[mid]:
                return True

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.search([1,3,1,1,1], 3))
