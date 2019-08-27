# class Solution:
#     def calculate(self, s: str) -> int:
#         operations = []
#         nums = []
#         i = 0
#         while i < len(s):
#             if s[i] != ' ':
#                 if s[i].isdigit():
#                     old_i = i
#                     while i < len(s) and s[i].isdigit():
#                         i += 1
#                     nums.append(int(s[old_i:i]))
#                 else:
#                     if not operations:
#                         operations.append(s[i])
#                     else:
#                         if s[i] in ('*', '/'):
#                             while operations and operations[-1] in ('*', '/'):
#                                 nums.append(operations.pop())
#                         else:
#                             while operations:
#                                 nums.append(operations.pop())
#                         operations.append(s[i])   
#                     i += 1
#             else:
#                 i += 1
#         while operations:
#             nums.append(operations.pop())
#         print(nums)
#         stack = []
#         for i in nums:
#             if type(i) == int:
#                 stack.append(i)
#             else:
#                 op1 = stack.pop()
#                 op2 = stack.pop()
#                 if i == '+':
#                     stack.append(op2 + op1)
#                 elif i == '-':
#                     stack.append(op2 - op1)
#                 elif i == '*':
#                     stack.append(op2 * op1)
#                 else:
#                     stack.append(op2 // op1)
#             print(stack)
#         return stack[-1]

class Solution:
    def calculate(self, s: str) -> int:
        current = 0
        high_num = 1
        high_op = '*'
        low_op = '+'
        low_num = 0
        for c in s:
            if c != ' ':
                if c.isdigit():
                    current = current * 10 + int(c)
                else:
                    if high_op == '*':
                        high_num *= current
                    else:
                        high_num //= current
                    current = 0
                    if c in '+-':
                        if low_op == '+':
                            low_num += high_num
                        else:
                            low_num -= high_num
                        high_num = 1
                        high_op = '*'
                        low_op = c
                    else:
                        high_op = c
        if high_op == '*':
            high_num *= current
        else:
            high_num //= current
        if low_op == '+':
            low_num += high_num
        else:
            low_num -= high_num
        return low_num

if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate("6-2+3"))