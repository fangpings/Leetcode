def longestPalindrome(s: 'str') -> 'str':
    try:
        current_long = s[0]
        global_long = current_long
    except IndexError:
        return ''
    all_same = True
    start = 0
    i = 0
    while i < len(s):
        if i == 0:
            i += 1
            continue
        if all_same:
            if s[i] == current_long[-1]:
                current_long += s[i]
                if len(current_long) > len(global_long):
                    global_long = current_long
                i += 1
                continue
        if start - 1 >= 0:
            if s[start-1] == s[i]:
                current_long = s[i] + current_long + s[i]
                start -= 1
                all_same = False
                if len(current_long) > len(global_long):
                    global_long = current_long
                i += 1
                continue
        if len(current_long) > 1:
            back = len(current_long) // 2
            current_long = s[i - back]
            all_same = True
            start = i - back
            i = i - back + 1
        else:
            current_long = s[i]
            all_same = True
            start = i
            i += 1

    return global_long


if __name__ == '__main__':
    print(longestPalindrome("a"), 'a')
    print(longestPalindrome("cbbd"), 'bb')
    print(longestPalindrome("aaaacaaaa"), 'aaaacaaaa')
    print(longestPalindrome("abababa"), 'abababa')
    print(longestPalindrome("anana"), 'anana')


        
