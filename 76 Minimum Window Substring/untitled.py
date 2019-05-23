from collections import defaultdict

class Solution:
    def minWindow(self, s, t):
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ''
        L = R = 0
        length = len(s)
        targets = defaultdict(int)
        total_targets = len(t)
        for c in t:
            targets[c] += 1
        while L < length and s[L] not in t:
            L += 1
        if L == length:
            return ''
        R = L + 1
        targets[s[L]] -= 1
        position = []
        total_targets -= 1
        while R < length and total_targets > 0:
            if s[R] in t:
                position.append(R)
                if targets[s[R]] > 0:
                    total_targets -= 1
                targets[s[R]] -= 1
            R += 1
        R -= 1
        if total_targets > 0:
            return ''
        min_len = R - L
        min_L = L
        min_R = R
        while R < length:     
            while targets[s[L]] < 0:
                targets[s[L]] += 1
                L = position.pop(0)
            target = s[L]
            if R - L < min_len:
                min_len = R - L
                min_L = L
                min_R = R
            targets[s[L]] += 1
            L = position.pop(0)
            while targets[s[L]] < 0:
                targets[s[L]] += 1
                L = position.pop(0)
            R += 1
            while R < length:
                if s[R] in t:
                    position.append(R)
                    targets[s[R]] -= 1
                if s[R] == target:
                    break
                R += 1
            if R == length:
                return s[min_L:min_R+1]
            else:
                if R - L < min_len:
                    min_len = R - L
                    min_L = L
                    min_R = R
        return s[min_L:min_R+1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.minWindow("abcabdebac", "cea"))




