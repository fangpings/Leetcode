class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        p = [0 for _ in range(K)]
        p[0] += 1
        pre_sum = 0
        for i in A:
            pre_sum += i
            p[pre_sum % K] += 1
        return int(sum([x*(x-1)/2 for x in p]))

        