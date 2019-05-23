def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    pal = 0
    ori = x
    while x > 0:
        pal = pal * 10 + x % 10
        x = x // 10
    if pal == ori:
        return True
    return False

# return str(x) == str(x)[::-1]

if __name__ == '__main__':
    print(isPalindrome(121), True)
    print(isPalindrome(0), True)
    print(isPalindrome(111), True)
    print(isPalindrome(-123), False)
    print(isPalindrome(10), False)
    print(isPalindrome(331), False)
    print(isPalindrome(1), True)