def nextPermutation(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 0 or len(nums) == 1:
        return nums
    start = len(nums) - 1
    while start > 0 and nums[start] <= nums[start-1]:
        start -= 1
    if start == 0:
        nums.reverse()
        return
    cur = start
    start -= 1
    while cur < len(nums) and nums[cur] > nums[start]:
        cur += 1
    cur -= 1
    nums[start], nums[cur] = nums[cur], nums[start]
    nums[start+1:] = sorted(nums[start+1:])

if __name__ == '__main__':
    a = [1,5,1]
    nextPermutation(a)
    print(a)
