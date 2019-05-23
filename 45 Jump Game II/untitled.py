def jump(nums):
    l = len(nums)
    if l <= 1:
        return 0
    if l == 2:
        return 1
    min_steps = [None for _ in range(l - 1)]
    def find_min(i):
        if min_steps[i] is None:
            if nums[i] == 0:
                min_steps[i] = 10000000000
            elif nums[i] >= l - 1 - i:
                min_steps[i] = 1
            else:
                tmp_min = 1000000000
                for j in range(min(nums[i], l), 0, -1):
                    if min_steps[i + j] + 1 < tmp_min:
                        tmp_min = min_steps[i + j] + 1
                        if tmp_min == 2:
                            break
                min_steps[i] = tmp_min
    for i in range(l - 2, -1, -1):
        find_min(i)
    return min_steps[0]

if __name__ == '__main__':
    print(jump([2,3,1,1,4]))