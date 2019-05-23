def permute(nums):
    ret = []
    if len(nums) == 1:
        return [nums]
    def rec(nums):
        if len(nums) == 1:
            return [nums]
        tmp = []
        for j in range(len(nums)):
            tmp += list(map(lambda x: [nums[j]] + x, rec(nums[:j] + nums[j+1:])))
        return tmp
    for j in range(len(nums)):
        ret += list(map(lambda x: [nums[j]] + x, rec(nums[:j] + nums[j+1:])))
    return ret

if __name__ == '__main__':
    print(permute([1]))
