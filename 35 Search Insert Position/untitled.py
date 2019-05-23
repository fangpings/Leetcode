def searchInsert(nums, target):
    if target == []:
        return 0
    if target > nums[-1]:
        return len(nums)
    if target < nums[0]:
        return 0

    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low > high:
        return low
    else:
        return high
if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 3))