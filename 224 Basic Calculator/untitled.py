class Solution:
    def calculate(self, s: str) -> int:
        operations = []
        nums = []
        i = 0
        while i < len(s):
            if s[i] != ' ':
                if s[i].isdigit():
                    old_i = i
                    while i < len(s) and s[i].isdigit():
                        i += 1
                    nums.append(int(s[old_i:i]))
                else:
                    if not operations:
                        operations.append(s[i])
                    else:
                        if s[i] == ')':
                            while operations[-1] != '(':
                                nums.append(operations.pop())
                            operations.pop()
                        else: 
                            if s[i] in '*/':
                                while operations and operations[-1] in '*/':
                                    nums.append(operations.pop())
                            
                            elif s[i] in '+-':
                                while operations and operations[-1] != '(':
                                    nums.append(operations.pop())
                            operations.append(s[i])   
                    i += 1
                print(nums, operations)
            else:
                i += 1
        while operations:
            nums.append(operations.pop())
        print(nums)
        stack = []
        for i in nums:
            if type(i) == int:
                stack.append(i)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if i == '+':
                    stack.append(op2 + op1)
                elif i == '-':
                    stack.append(op2 - op1)
                elif i == '*':
                    stack.append(op2 * op1)
                else:
                    stack.append(op2 // op1)
        return stack[-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate('2*3*4'))