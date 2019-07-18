from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        left, right = -1, 0
        distinct = 0
        hashmap = defaultdict(int)
        ret = 0
        while right < l:
            if hashmap[s[right]] == 0:
                hashmap[s[right]] += 1
                distinct += 1
                while distinct > 2:
                    left += 1
                    hashmap[s[left]] -= 1
                    if hashmap[s[left]] == 0:
                        distinct -= 1
            else:
                hashmap[s[right]] += 1
            if right - left > ret:
                ret = right - left
            right += 1
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstringTwoDistinct("abcde"))