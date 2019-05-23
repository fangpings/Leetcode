def searchRange(nums, target):
    low, high = 0, len(nums) - 1
    pre_low, pre_high = low, high
    ret = [-1, -1]
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            ret = [mid, mid]
            low1, high1 = pre_low, mid - 1
            while low1 <= high1:
                mid1 = (high1 + low1) // 2
                if nums[mid1] == target:
                    ret[0] = mid1
                    high1 = mid1 - 1
                else:
                    # nums[mid1] > target cannot happen
                    low1 = mid1 + 1
            low2, high2 = mid + 1, pre_high
            while low2 <= high2:
                mid2 = (high2 + low2) // 2
                if nums[mid2] == target:
                    ret[1] = mid2
                    low2 = mid2 + 1
                else:
                    high2 = mid2 - 1
            return ret
        elif nums[mid] < target:
            pre_low, pre_high = low, high
            low = mid + 1
        else:
            pre_low, pre_high = low, high
            high = mid - 1
    return ret

if __name__ == '__main__':
    print(searchRange([2, 2], 2))