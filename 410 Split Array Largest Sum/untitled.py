# class Solution:
#     def splitArray(self, nums, m):
#         if m == len(nums):
#             return max(nums)
#         l = len(nums)
#         all_sum = [[-1 for _ in range(l)] for _ in range(l)]
#         for i in range(l):
#             for j in range(i, l):
#                 all_sum[i][j] = sum(nums[i:j+1])
#         s = [[0 for _ in range(m + 1)] for _ in range(l)]
#         for i in range(m - 1, l):
#             s[i][1] = all_sum[i][-1]
#         for k in range(2, m + 1):
#             for i in range(m - k, l - k + 1):
#                 s[i][k] = min([max(all_sum[i][j], s[j+1][k-1]) for j in range(i, l - k + 1)])
#         return s[0][-1]

class Solution:
    def splitArray(self, nums, m):
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            print(mid)
            if self.feasible(nums, mid, m):
                r = mid - 1
            else:
                l = mid + 1
        if self.feasible(nums, l, m):
            return l
        else:
            return l + 1

    def feasible(self, nums, k, m):
        acc = 0
        count = 1
        for i in nums:
            if acc + i > k:
                if i > k:
                    return False
                acc = i
                count += 1
                if count > m:
                    return False
            else:
                acc += i
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.splitArray([7,2,5,10,8], 1))
