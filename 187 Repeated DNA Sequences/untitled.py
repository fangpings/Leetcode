from collections import defaultdict
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        dic = defaultdict(int)
        for i in range(len(s) - 10 + 1):
            dic[s[i:i+10]] += 1
        ret = []
        print(dic)
        for x, count in dic.items():
            if count > 1:
                ret.append(x)
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
