def firstMissingPositive(nums):
    nums.append(0)
    l = len(nums)
    for i in range(l):
        if nums[i] < 0 or nums[i] >= l:
            nums[i] = 0
    for i in range(l):
        nums[nums[i] % l] += l
    for i in range(1, l):
        if nums[i] // l == 0:
            return i
    return l

if __name__ == '__main__':
    print(firstMissingPositive([2,2]))

