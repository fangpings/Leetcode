def maxSubArray(nums):
    l = len(nums)
    if l == 0:
        return None
    dp = [nums[0]]
    for i in range(1, l):
        tmp = dp[-1] if dp[-1] > 0 else 0
        dp.append(tmp + nums[i])
    return max(dp)

if __name__ == '__main__':
    print(maxSubArray([-2,-1,-2]))


