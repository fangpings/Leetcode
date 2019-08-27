### 227 Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only **non-negative** integers, `+`, `-`, `*`, `/`operators and empty spaces ``. The integer division should truncate toward zero.

**Example 1:**

```
Input: "3+2*2"
Output: 7
```

**Example 2:**

```
Input: " 3/2 "
Output: 1
```

**Example 3:**

```
Input: " 3+5 / 2 "
Output: 5
```

**Note:**

- You may assume that the given expression is always valid.
- **Do not** use the `eval` built-in library function.

### 想法

没有括号，说明深度最多为1了（加减在下，乘除在上）。**所以我们不再需要栈了**。我们只需要维护五个变量:当前处理的数，乘除的上一个操作数，乘除的上一个操作符号，加减的上一个操作数，加减的上一个符号。

每当我们碰到一个符号，我们先把当前处理的操作数和乘除的上一个操作数和符号做处理（这是为了先处理乘除，类似1+2*3+1这种情况，我们要优先处理乘号）然后我们再来判断当前的符号是什么，如果是乘除，我们因为已经处理过了，所以只要把乘除的上一个操作符号设为当前符号就可以（等待下一个操作数来处理）。如果是加减，那么说明当前的乘除操作已经结束了，我们计算加减，并重新把乘法上一个操作数设为1，上一个操作符号设为\*（这样就说明乘法没有上一个操作数和符号）

总体的想法就是利用四个变量来代替栈，注意这个变量的初始化还是挺有意思的。

```python
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
```

