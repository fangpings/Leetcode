def NSum(nums, N, target):
    def NSum_recursive(nums, N, target):
        # nums must be sorted
        result = []
        # the following line has huge impact on performance
        try:
            if nums[0] * N > target or nums[-1] * N < target:
                return result
        except:
            pass
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while  l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            i = 0
            while i < len(nums) - (N - 1):
                result += [x + [nums[i]] for x in NSum(nums[i + 1:], N - 1, target - nums[i])]
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
        return result 
    return NSum_recursive(sorted(nums), N, target)



if __name__ == '__main__':
    print(NSum([0,0,0,0], 4, 0))


