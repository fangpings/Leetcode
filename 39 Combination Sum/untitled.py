def combinationSum(candidates, target):
    ret = []
    def rec(candidates, target, s):
        for n, i in enumerate(candidates):
            if i > target:
                return
            elif i == target:
                ret.append(s + [i])
                return
            else:
                rec(candidates[n:], target - i, s + [i])
    candidates.sort()
    rec(candidates, target, [])
    return ret

if __name__ == '__main__':
    print(combinationSum([], 5))


