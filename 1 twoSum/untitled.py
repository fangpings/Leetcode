def twoSum(nums: 'List[int]', target: 'int') -> 'List[int]':
    hashmap = {}
    for i, num in enumerate(nums):
        if num in hashmap:
            if num * 2 == target:
                return [hashmap[num], i]
        else:
            hashmap[num] = i
    for num in nums:
        if target - num == num:
            continue
        if target - num in hashmap:
            return [hashmap[num], hashmap[target - num]]


if __name__ == '__main__':
    test = [3, 2, 4]
    print(twoSum(test, 6))
