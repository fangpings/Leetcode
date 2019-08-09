class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(s) for s in version1.split('.')]
        v2 = [int(s) for s in version2.split('.')]
        reverse = False
        if len(v1) > len(v2):
            v1, v2 = v2, v1
            reverse = True
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return -1 if reverse else 1
            elif v1[i] < v2[i]:
                return 1 if reverse else -1
        for i in range(len(v1), len(v2)):
            if v2[i] > 0:
                return 1 if reverse else -1
        return 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.compareVersion('0.1', '1.1'), -1)
    print(sol.compareVersion('1.0.1', '1'), 1)
    print(sol.compareVersion('7.5.2.4', '7.5.3'), -1)
    print(sol.compareVersion('1.01', '1.001'), 0)
    print(sol.compareVersion('1.0', '1.0.0'), 0)
