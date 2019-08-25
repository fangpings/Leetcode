class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return []
        product = 1
        ret = []
        for i in nums:
            product *= i
            ret.append(product)
        product = 1
        for i in range(len(nums) - 1, 0, -1):
            ret[i] = ret[i-1] * product
            product *= nums[i]
        ret[0] = product
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1,2]))

