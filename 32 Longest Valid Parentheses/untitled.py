def longestValidParentheses(s):
    check = [0 for _ in range(len(s))]
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        if c == ')' and len(stack):
            check[stack.pop()] = 1
            check[i] = 1
    max_len = 0
    i = 0
    while i < len(check):
        if check[i]:
            tmp = 0
            while i < len(check) and check[i]:
                tmp += 1
                i += 1
            if tmp > max_len:
                max_len = tmp
        i += 1
    return max_len

if __name__ == '__main__':
    print(longestValidParentheses("(((((("))

