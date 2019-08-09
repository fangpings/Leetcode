class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if lower == upper:
            if lower in nums:
                return []
            else:
                return [str(lower)]
        if not nums:
            return [str(lower) + '->' + str(upper)]
        ret = []
        last = lower - 1
        for i in nums:
            if i < lower:
                continue
            elif i > upper:
                if upper - last == 1:
                    ret.append(str(upper))
                elif upper - last > 1:
                    ret.append(str(last + 1) + '->' + str(upper))
                break
            else:
                if i - last <= 1:
                    last = i
                elif i - last == 2:
                    ret.append(str(i - 1))
                else:
                    ret.append(str(last + 1) + '->' + str(i - 1))
                last = i
        if i < upper:
            if upper - last == 1:
                ret.append(str(upper))
            else:
                ret.append(str(last + 1) + '->' + str(upper))
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMissingRanges([0,1,2,3], 1, 2), [])
    print(sol.findMissingRanges([0,2,3], 1, 2), ['1'])
    print(sol.findMissingRanges([0,1,3], 1, 2), ['2'])
    print(sol.findMissingRanges([0,3], 1, 2), ['1->2'])
    print(sol.findMissingRanges([0], 1, 2), ['1->2'])
    print(sol.findMissingRanges([1], 1, 2), ['2'])
    print(sol.findMissingRanges([2], 1, 2), ['1'])
    print(sol.findMissingRanges([3], 1, 2), ['1->2'])
    print(sol.findMissingRanges([], 1, 2), ['1->2'])
    print(sol.findMissingRanges([0,2,3], 1, 3), [])


