def lengthOfLongestSubstring(s: 'str') -> 'int':
    if len(s) == 0:
        return 0
    max_len = 1
    current_long = ''
    for c in s:
        if c not in current_long:
            current_long += c
        else:
            current_long = current_long.split(c)[-1] + c
        if len(current_long) > max_len:
            max_len = len(current_long)
    return max_len

if __name__ == '__main__':
    print(lengthOfLongestSubstring("ohvhjdml"))