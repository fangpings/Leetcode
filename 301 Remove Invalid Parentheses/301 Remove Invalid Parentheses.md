### 301 Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

**Note:** The input string may contain letters other than the parentheses `(` and `)`.

**Example 1:**

```
Input: "()())()"
Output: ["()()()", "(())()"]
```

**Example 2:**

```
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
```

**Example 3:**

```
Input: ")("
Output: [""]
```

### 想法

这题真的挺难的。。先把代码放上来

```python
class Solution:
    def removeInvalidParentheses(self, s):
        self.ret = []
        self.remove_one(s, 0, 0, ('(', ')'))
        return self.ret

    def remove_one(self, s, last_i, last_j, bracket):
        stack = 0
        for i in range(last_i, len(s)):
            if s[i] == bracket[0]:
                stack += 1
            if s[i] == bracket[1]:
                stack -= 1
            if stack >= 0:
                continue
            for j in range(last_j, i + 1):
                if s[j] == bracket[1] and (j == last_j or s[j-1] != bracket[1]): #总是选择连续括号的第一个或者上一次j的下一个
                    self.remove_one(s[:j] + s[j+1:], i, j, bracket) # 这里因为j位置的字符已经去掉了，所以i,j都自动+1了
            return # 我们一次只删一个，剩下的交给后面的递归去做
        s = s[::-1] # 如果没转过我们反向把左括号去了，如果转过了我们再转回来
        if bracket[0] == '(':
            self.remove_one(s, 0, 0, (')', '('))
        else:
            self.ret.append(s)
```

想法是这样的，我们**先考虑右括号不对的情况**。我们用stack来表示右括号的情况，每当我们遇到左括号，我们的stack+1，每当遇到右括号，stack-1，当stack的值小于0的时候，说明右括号多于左括号了，注意这个问题是没办法在后面解决的，即如果某个节点stack小于0，必然说明这个节点以及之前的右括号有问题。然后我们考虑删掉出问题的右括号（因为一小于0我们就着手解决，所以只需要删掉一个右括号就行了），删掉的右括号我们可以有多个选择，**实际上在出问题的右括号（包括）之前的所有右括号都可以删掉**，但是连续的右括号删掉哪个效果是一样的，**所以我们选择删掉连续右括号的第一个**。因为有多种选择，所以我们递归的删掉所有可能的右括号，然后重新调用这个函数，从当前位置开始继续查找出问题的右括号（这个位置对应的是i index），如果查找到了下一个位置右括号又多了，那我们继续删除，但是这次删除是从上次删除的地方开始继续查找右括号的（这里对应j index），**因为前面的所有右括号必定已经在其他的递归中被删掉过了，所以我们不需要考虑前面的右括号了**（这一个真的很绕，因为我们不论删掉哪个，下次递归碰到的出问题的右括号的位置都是相同的，那前面的递归就会替我们考虑删掉前面位置的右括号的情况）。**因为递归会一路做到头，所以我们删掉之后就直接return就行了，除非已经没有出问题的右括号了，那我们不会到达return这一句。**

然后我们来考虑出问题的左括号，**这里就非常聪明了，我们把整个字符串反向，然后open bracket变成右括号，close bracket变成左括号，然后重新做整个操作就可以删掉所有出问题的左括号了。**