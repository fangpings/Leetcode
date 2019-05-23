def generateParenthesis(n):
    def recursive(n, results, stack_top, string):
        if n == 0:
            results.append(string + ')' * stack_top)
        else:
            if stack_top > 0:
                recursive(n, results, stack_top - 1, string + ')')
            recursive(n - 1, results, stack_top + 1, string + '(')
    if n == 0:
        return []
    results = []
    recursive(n, results, 0, '')
    return results

if __name__ == '__main__':
    print(generateParenthesis(3))