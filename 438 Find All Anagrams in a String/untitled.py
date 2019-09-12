from collections import defaultdict
from copy import deepcopy

class Solution:
    def findAnagrams(self, s, p):
        if not p or not s:
            return []
        lp = len(p)
        ls = len(s)
        pos = defaultdict(list)
        hashmap_count = defaultdict(int)
        alphabet = set(p)
        for c in p:
            hashmap_count[c] += 1
        count = deepcopy(hashmap_count)

        left = 0
        right = -1
        ret = []
        while left < ls - lp + 1:
            if right - left + 1 < lp:
                right += 1
                if s[right] not in alphabet:
                    left = right + 1
                    pos = defaultdict(list)
                    count = deepcopy(hashmap_count)
                    continue
                elif count[s[right]] == 0:
                    next_pos = pos[s[right]][0] + 1
                    while left < next_pos:
                        count[s[left]] += 1
                        pos[s[left]].pop(0)
                        left += 1
                count[s[right]] -= 1
                pos[s[right]].append(right)
            else:
                ret.append(left)
                count[s[left]] += 1
                pos[s[left]].pop(0)
                left += 1
        return ret

if __name__ == '__main__':
     sol = Solution()
     print(sol.findAnagrams("abab", 'ab')) 


