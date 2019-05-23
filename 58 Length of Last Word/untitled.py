def lengthOfLastWord(s):
    ret = 0
    l = len(s)
    i = l - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ' :
        i -= 1
        ret += 1
    return ret

if __name__ == '__main__':
    print(lengthOfLastWord(""))