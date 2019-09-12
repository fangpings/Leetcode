from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        count = defaultdict(int)
        left, right = 0, 0
        max_length = 0
        current_count = 0
        while right < len(s):
            count[s[right]] += 1
            if count[s[right]] == 1:
                current_count += 1
            if current_count <= k:
                max_length = max(right - left + 1, max_length)
            else:
                while left <= right:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        current_count -= 1
                        left += 1
                        break
                    else:
                        left += 1
            right += 1
        return max_length

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstringKDistinct("aaabbbc", 2))



