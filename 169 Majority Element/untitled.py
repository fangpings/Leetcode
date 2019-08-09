from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = 0
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
            if dic[i] > majority:
                majority = dic[i]
                element = i
        return element

