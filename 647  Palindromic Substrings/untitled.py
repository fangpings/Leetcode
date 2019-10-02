class Solution:
    def countSubstrings(self, s: str) -> int:
        s1 = [True for _ in range(len(s))]
        s2 = [True for _ in range(len(s))]
        count = 0
        for l in range(2, len(s) + 1):
            s1, s2 = s2, [s1[i+1] and s[i] == s[i+l-1] for i in range(len(s) - l + 1)]
            count += sum(s1)
        return count + sum(s2)

if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings(''))