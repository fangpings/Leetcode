class Solution:
    def lengthOfLIS(self, nums):
        self.tails = []
        for i in nums:
            self.binary_search(i)
        return len(self.tails)

    def binary_search(self, num):
        l, r = 0, len(self.tails) - 1
        while l <= r:
            mid = (l + r) // 2
            if num > self.tails[mid]:
                l = mid + 1 
            else:
                r = mid - 1
        if l == len(self.tails):
            self.tails.append(num)
        else:
            self.tails[l] = num

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS([9,8,6,7]))