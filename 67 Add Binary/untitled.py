class Solution:
    def addBinary(self, a, b):
        la, lb = len(a), len(b)
        carry = 0
        ret = ''
        l = min(la, lb)
        i = -1
        while i >= -l:
            if a[i] == '1' and b[i] == '1':
                if carry:
                    ret = '1' + ret
                else:
                    ret = '0' + ret
                    carry = 1
            elif a[i] == '0' and b[i] == '0':
                if carry:
                    ret = '1' + ret
                    carry = 0
                else:
                    ret = '0' + ret
            else:
                if carry:
                    ret = '0' + ret
                else:
                    ret = '1' + ret
            i -= 1
        l = max(la, lb)
        s = a if la > lb else b
        while i >= -l:
            if s[i] == '1':
                if carry:
                    ret = '0' + ret
                else:
                    ret = '1' + ret
            else:
                if carry:
                    ret = '1' + ret
                    carry = 0
                else:
                    ret = '0' + ret
            i -= 1
        if carry:
            ret = '1' + ret
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary('1111', '1'))
