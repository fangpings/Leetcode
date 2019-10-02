class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        plus = [0]
        minus = [0]
        maximum = -1000000000
        for i in nums:
            if i > 0:
                tp = plus[-1]
                tm = minus[-1]
                plus.append(max(tp * i, i))
                minus.append(tm * i)
            elif i < 0:
                tp = plus[-1]
                tm = minus[-1]
                plus.append(tm * i)
                minus.append(min(tp * i, i))
            else:
                plus.append(0)
                minus.append(0)
            maximum = max(maximum, plus[-1], minus[-1])
        return maximum

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct([-2, 1]))