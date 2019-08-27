class Solution:
    def findKthLargest(self, nums, k):
        return self.rec(nums, 0, len(nums) - 1, k)

    def rec(self, nums, i, j, k):
        if i == j:
            return nums[i]
        mid = (i + j) // 2
        num_mid = nums[mid]
        old_i, old_j = i, j
        nums[mid], nums[i] = nums[i], nums[mid]
        i += 1
        while i < j:
            while i < j and nums[i] >= num_mid:
                i += 1
            while i < j and nums[j] < num_mid:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        if nums[i] < num_mid:
            i -= 1
        nums[old_i], nums[i] = nums[i], nums[old_i]
        # print(i, old_i, old_j)
        if i == k - 1:
            return nums[i]
        elif i > k - 1:
            return self.rec(nums, old_i, i-1, k)
        else:
            return self.rec(nums, i+1, old_j, k)

if __name__ == '__main__':
    sol = Solution()
    nums = [1]
    for i in range(1, len(nums) + 1):
        print(sol.findKthLargest(nums, i))