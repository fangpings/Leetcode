def removeDuplicates(nums):
    if nums == []:
        return 0
    cur1 = 0
    cur2 = 0
    tmp = nums[0]
    l = len(nums)
    while True:
        while cur2 < l and nums[cur2] == tmp:
            cur2 +=1
        if cur2 == l:
            return cur1 + 1
        tmp = nums[cur2]
        cur1 += 1
        nums[cur1] = tmp

if __name__ == '__main__':
    test = []
    a = removeDuplicates(test)
    print(test[:a])