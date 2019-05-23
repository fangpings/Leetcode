def canJump(nums):
    l = len(nums)
    if l <= 1:
        return True
    last_index, next_index = 0, nums[0]
    while next_index < l - 1:
        print(last_index, next_index)
        if last_index == next_index:
            return False
        last_index, next_index = next_index, max([i + nums[i] for i in range(last_index, next_index + 1)])
    return True

if __name__ == '__main__':
    print(canJump([2,2,0,2,0,2,0,0,2,0]))