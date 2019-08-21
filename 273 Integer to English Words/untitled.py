class Solution:
    def numberToWords(self, num):
        if num == 0:
            return 'Zero'
        num = str(num) + ' '
        big = ['', 'Thousand', 'Million', 'Billion']
        i = 1
        ret = ''
        while i <= len(num):
            tmp = self.trinity(num[-(i+3):-i])
            if tmp:
                if ret:
                    ret = ' ' + ret
                if i > 1:
                    ret = tmp + ' ' + big[i//3] + ret
                else:
                    ret = tmp
            i += 3
        return ret

    def trinity(self, num):
        if num == '000':
            return ''
        num = '0' * (3 - len(num)) + num
        units = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        one_tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        ret = ''
        if num[0] != '0':
            ret += units[int(num[0])] + ' ' + 'Hundred'
            if num[1] == '0':
                if num[2] == '0':
                    return ret
                else:
                    return ret + ' ' + units[int(num[-1])]
        if num[1] != '0':
            if ret:
                ret += ' '
            if num[1] == '1':
                return ret + one_tens[int(num[2])]
            else:
                ret += tens[int(num[1])]
        if num[2] != '0':
            if ret:
                ret += ' '
            ret += units[int(num[2])]
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.numberToWords(123))





