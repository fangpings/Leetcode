class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        if k == 1:
            return nums
        l = len(nums)
        left_max, right_max = [0 for _ in range(l)], [0 for _ in range(l)]
        for i in range(l // k + 1):
            tmp_max = -2**32
            for j in range(0, min(k, l - i * k)):
                tmp_max = max(tmp_max, nums[i*k+j])
                left_max[i*k+j] = tmp_max
        for i in range(l // k, -1, -1):
            tmp_max = -2**32
            for j in range(min(k, l - i * k) - 1, -1, -1):
                tmp_max = max(tmp_max, nums[i*k+j])
                right_max[i*k+j] = tmp_max
        print(left_max)
        print(right_max)
        ret = [0 for _ in range(l - k + 1)]
        for i in range(l - k + 1):
            ret[i] = max(right_max[i], left_max[i + k - 1])
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSlidingWindow([1,2], 2))