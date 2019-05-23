class Solution:
    def plusOne(self, digits):
        l = len(digits)
        carry = 1
        for i in range(l-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
                break
        if carry:
            digits.insert(0, 1)
        return digits

if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([2,5,9,9]))