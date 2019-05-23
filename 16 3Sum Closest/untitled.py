from collections import defaultdict

def threeSumClosest(nums, target):

    if len(nums) == 3:
        return sum(nums)

    maxvalue = 1e10
    minvalue = -1e10
    def binary_search(array, target):
        n = len(array)
        left = 0
        right = n - 1
        while True:
            mid = (right + left) // 2
            if array[mid] > target:
                right = mid - 1
            elif array[mid] < target:
                left = mid + 1
            else:
                return None
            if left + 1 >= right:
                if target in (array[left], array[right]):
                    return None
                if left == 0 and target < array[left]:
                    return (minvalue, array[0])
                if right == n - 1 and target > array[right]:
                    return (array[-1], maxvalue)
                return (array[left], array[right])

    repeated_count = defaultdict(int)
    new = nums
    for i in nums:
        repeated_count[i] += 1
        # if repeated_count[i] == 1:
        #     new.append(i)

    i = 0
    l = len(new)
    best = 1e10
    new = sorted(new)
    while i < l:
        j = 0
        while j < l:
            if (new[i] == new[j] and repeated_count[new[i]] >= 2) or new[i] != new[j]:
                diff = target - new[i] - new[j]
                search = binary_search(new, diff)
                if search:
                    if abs(diff - search[0]) < abs(best - target):
                        if (search[0] in (new[i], new[j]) and repeated_count[search[0]] >= 2) or search[0] not in (new[i], new[j]):
                            best = new[i] + new[j] + search[0]
                    if abs(diff - search[1]) <abs(best - target):
                        if (search[1] in (new[i], new[j]) and repeated_count[search[1]] >= 2) or search[1] not in (new[i], new[j]):
                            best = new[i] + new[j] + search[1]
                else:
                    if diff in (new[i], new[j]):
                        if new[i] == new[j]:
                            if repeated_count[diff] >= 3:
                                return target
                    else:
                        return target
            j += 1
        i += 1
    return best

if __name__ == '__main__':
    print(threeSumClosest([-1, 0, 1, 1, 55], 3))