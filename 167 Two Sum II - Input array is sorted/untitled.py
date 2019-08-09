class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return l + 1, r + 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([1,2,3,4], 7))