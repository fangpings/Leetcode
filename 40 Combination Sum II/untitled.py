def combinationSum(candidates, target):
    ret = []
    def rec(candidates, target, s):
        k = 0
        l = len(candidates)
        while k < l:
            i = candidates[k]
            if i > target:
                return
            elif i == target:
                ret.append(s + [i])
                return
            else:
                rec(candidates[k+1:], target - i, s + [i])
            while k + 1 < l and candidates[k] == candidates[k+1]:
                k += 1
            k += 1
    candidates.sort()
    rec(candidates, target, [])
    return ret

if __name__ == '__main__':
    print(combinationSum([], 5))


