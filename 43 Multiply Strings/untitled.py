def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return 0
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    l1, l2 = len(num1), len(num2)
    num1 = num1[::-1]
    num2 = num2[::-1]
    ret = ''
    carry = 0
    for i in range(l1 + l2 - 1):
        num = 0
        for j in range(max(0, i - l1 + 1), min(i, l2 - 1) + 1):
            num += int(num2[j]) * int(num1[i-j])
        num += carry
        ret = str(num % 10) + ret
        carry = num // 10
    if carry > 0:
        ret = str(carry) + ret
    return ret

if __name__ == '__main__':
    print(multiply('100', '10'))
