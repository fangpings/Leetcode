# def isMatch(s: str, p: str) -> bool:
#     ps = 0
#     pp = 0
#     ls = len(s)
#     lp = len(p)
#     if s == '':
#         try:
#             if p[1] == '*' or p == '':
#                 return True
#             else:
#                 return False
#         except:
#             return False
#     while ps < ls and pp < lp:
#         try:
#             if p[pp + 1] == '*':
#                 if p[pp] == '.':
#                     new_pp = pp + 3
#                     while new_pp + 2 < ls and p[new_pp] == '*':
#                         new_pp += 2
#                     if new_pp == ls:
#                         return True
#                     else:
#                         while ps < ls and s[ps] != p[new_pp]:
#                             ps += 1
#                 while ps < ls and p[pp] == s[ps]:
#                     ps += 1
#                 pp += 2
#             elif p[pp] == '.' or p[pp] == s[ps]:
#                 pp += 1
#                 ps += 1
#             else:
#                 return False
#         except:
#             if ps == ls - 1:
#                 if p[pp] == '.' or p[pp] == s[ps]:
#                     return True
#                 else:
#                     return False
#             else:
#                 return False
#     if ps != ls:
#         return False
#     else:
#         while pp < lp:
#             try:
#                 if p[pp + 1] == '*':
#                     pp += 2
#                 else:
#                     return False
#             except:
#                 return False
#         return True

def isMatch(s: str, p: str) -> bool:
    if p == '':
        if s == '':
            return True
        else:
            return False
    splp = p.split('*')
    if s == '':
        for subp in splp[:-1]:
            if len(subp) != 1:
                return False
        if splp[-1] != '':
            return False
        return True
    if len(splp) == 1:
        if len(s) != len(p):
            return False
        for i in range(min(len(s), len(p))):
            if p[i] == '.':
                continue
            elif s[i] != p[i]:
                return False
        return True
    for i, subp in enumerate(splp[:-1]):
        l = len(subp)
        if l > 1:
            if len(s) < l - 1:
                 return False  
            for j in range(len(subp[:-1])):
                if subp[j] == '.':
                    continue
                elif subp[j] != s[j]:
                    return False
        s = s[l-1:]
        if subp[-1] == '.':
            for j in range(len(s)):
                if isMatch(s[j:], '*'.join(splp[i+1:])):
                    return True
            return isMatch('', '*'.join(splp[i+1:]))
        else:
            j = 0
            while j < len(s):
                if isMatch(s[j:], '*'.join(splp[i+1:])):
                        return True
                if s[j] != subp[-1]:
                    break
                j += 1
            if j == len(s):
                return isMatch('', '*'.join(splp[i+1:]))
            else:
                s = s[j:]
    return isMatch(s, splp[-1])

if __name__ == '__main__':
    print(isMatch('aa', 'a') == False)
    print(isMatch('aa', 'a*') == True)
    print(isMatch('ab', '.*') == True)
    print(isMatch('aab', 'c*a*b') == True)
    print(isMatch('mississippi', 'mis*is*p*.') == False)
    print(isMatch('', 'dsf') == False)
    print(isMatch('', 's*') == True)
    print(isMatch('ab', '.*c') == False)
    print(isMatch('ab', '.*.*c') == False)
    print(isMatch('ab', '.*.*') == True)
    print(isMatch('ab', '.*c*') == True)
    print(isMatch('ab', '.*.*f') == False)
    print(isMatch('ab', '.*.') == True)
    print(isMatch('abc', '.*.c') == True)
    print(isMatch('a', 'ab*') == True)
    print(isMatch('a', '.*..a*') == False)
    





