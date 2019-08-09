class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) <= 1:
            return 0
        max_val, min_val = max(nums), min(nums)
        bucket_num = len(nums) - 1
        bucket_size = (max_val - min_val) // bucket_num + 1
        buckets = [None for _ in range(bucket_num)]
        for i in nums:
            index = (i - min_val) // bucket_size 
            if buckets[index]:
                buckets[index][0] = min(i, buckets[index][0])
                buckets[index][1] = max(i, buckets[index][1])
            else:
                buckets[index] = [i, i]
        max_interval = -10000
        buckets = [bucket for bucket in buckets if bucket]
        for i in range(len(buckets) - 1):
            max_interval = max(buckets[i+1][0] - buckets[i][1], max_interval)
        return max(max_interval, max([bucket[1] - bucket[0] for bucket in buckets]))

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumGap([5,5,5]))


         
