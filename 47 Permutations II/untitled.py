def permuteUnique(nums):
    nums.sort()
    def rec(nums):
        if len(nums) == 1:
            return [nums]
        ret = []
        l = len(nums)
        j = 0
        while j < l:
            ret += list(map(lambda x: [nums[j]] + x, rec(nums[:j] + nums[j+1:])))
            while j < l - 1 and nums[j] == nums[j+1]:
                j += 1
            j += 1
        return ret
    return rec(nums)

if __name__ == '__main__':
    print(permuteUnique([1,1]))