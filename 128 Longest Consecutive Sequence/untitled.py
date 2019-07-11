class Solution:
    def longestConsecutive(self, nums):
        mapping = set(nums)
        longest = 0
        for num in mapping:
            if num - 1 not in mapping:
                current_num = num
                current = 1

                while current_num + 1 in mapping:
                    current_num += 1
                    current += 1

                if current > longest:
                    longest = current
        return longest

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([]))