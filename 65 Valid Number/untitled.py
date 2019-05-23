class Solution:
    def isNumber(self, s):
        # regular expression for a valid number
        # s = s.strip()
        # spl = s.split('.')
        # if len(spl) > 2:
        #     return False
        # if len(spl) == 2:
        #     a, b = spl[0], spl[1]
        #     la = len(a)
        #     if len(a) == 0 and len(b) == 0:
        #         return False
        #     i = 0
        #     if s[i] in ['-', '+']:
        #         i += 1
        #     while i < la:
        #         if not s[i].isdigit():
        #             return False
        #         i += 1
        #     spl = b.split('e')
        #     if len(spl) > 2:
        #         return False
        #     if len(spl) == 2:
        #         a, b = spl[0], spl[1]


        s = s.strip()
        l = len(s)
        if l == 0:
            return False
        i = 0
        if s[i] in ['-', '+']:
            i +=1
            if i == l:
                return False
        len_flag = False
        if s[i].isdigit():
            while i < l:
                if not s[i].isdigit():
                    if s[i] in ['.', 'e']:
                        break
                    else:
                        return False
                i += 1
            if i == l:
                return True
        elif s[i] == '.':
            len_flag = True
        else:
            return False
        if s[i] == '.':
            i += 1
            if len_flag and (i == l or not s[i].isdigit()):
                return False
            while i < l:
                if not s[i].isdigit():
                    if s[i] == 'e':
                        break
                    else:
                        return False
                i += 1
            if i == l:
                return True
        i += 1
        if i == l:
            return False
        if s[i] in ['-', '+']:
            i += 1
        if i == l:
            return False
        while i < l:
            if not s[i].isdigit():
                return False
            i += 1
        return True

if __name__ == '__main__':
    sol = Solution()
    test = ["0", " 0.1 ", "abc", "1 a", "2e10", " -90e3   ", " 1e", "e3", " 6e-1", " 99e2.5 ", "53.5e93", " --6 ", "-+3", "95a54e53", "+", "1e+", "1e-+5", "1.53e", '   ', '', '.1', '-.1', '3.', '3.e5', '.']
    for s in test:
        print(s, sol.isNumber(s))

