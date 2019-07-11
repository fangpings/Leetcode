class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c1 = 0
        c2 = 0
        m = 0
        for i in nums:
            c2 ^= c1 & i
            c1 ^= i
            mask = ~(c1 & c2) # k = 3, 二进制形式为11，则c1和c2都不用取反
            c1 &= mask
            c2 &= mask
        return c1 # p = 1, 则最后c1 = single
        