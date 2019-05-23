def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    total = numRows * 2 - 2
    vertical = numRows
    horizontal = numRows - 1
    strs = ['' for _ in range(vertical)]
    s = s + ' ' * (total - len(s) % total)
    for i in range(len(s)//total):
        tmp_slice = s[i*total:(i+1)*total]
        for j in range(vertical):
            tmp = ['' for _ in range(horizontal)]
            tmp[0] = tmp_slice[j]
            if j > 0 and j < vertical - 1:
                tmp[-j] = tmp_slice[-j]
            strs[j] += ''.join(tmp)
    return ''.join(strs).replace(' ', '')

# class Solution:
#     def convert(self, s: 'str', numRows: 'int') -> 'str':
#         if numRows==1 :
#            return s
#        row = 0
#        d = 1 # direction
#        data=[ "" ]*numRows
#        for c in s:
#            data[row]= data[row] + c
#            if row==0:
#               d = 1
#            elif  row==numRows-1 :
#               d = -1
#            row = row + d
#        st = ""
#        for k in data:
#           st=st+k
#        return st

if __name__ == '__main__':
    print(convert('ffaa', 2))
            
