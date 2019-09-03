from random import randint

class Solution:

    def __init__(self, w):
        self.acc_sum = [0]
        acc = 0
        for i in w:
            acc += i
            self.acc_sum.append(acc)
        self.max = acc

    def pickIndex(self):
        target = randint(0, self.max - 1)
        i, j = 0, len(self.acc_sum) - 2
        while i <= j:
            mid = (i + j) // 2
            if self.acc_sum[mid] == target:
                return mid
            elif self.acc_sum[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return j

def bi(nums, target):
    assert len(nums) >= 2
    i, j = 0, len(nums) - 2
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            i = mid + 1
        else:
            j = mid - 1
    return j

if __name__ == '__main__':
    print(bi([0,3,5,8], 3))
