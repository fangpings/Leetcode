class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        while tokens:
            token = tokens.pop(0)
            if token in '+-*/':
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand2 - operand1)
                elif token == '*':
                    stack.append(operand1 * operand2)
                else:
                    if operand1 * operand2 < 0:
                        stack.append(-(-operand2 // operand1))
                    else:
                        stack.append(operand2 // operand1)
            else:
                stack.append(int(token))
            print(stack)
        return stack.pop()

if __name__ == '__main__':
    sol = Solution()
    print(sol.evalRPN(["4", "13", "5", "/", "+"]))