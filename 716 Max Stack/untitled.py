from collections import defaultdict

class ListNode(object):
    """docstring for ListNode"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if not self.stack2:
            self.stack2.append(x)
        else:
            self.stack2.append(max(self.stack2[-1], x))

    def pop(self) -> int:
        self.stack2.pop()
        return self.stack1.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def peekMax(self) -> int:
        return self.stack2[-1]

    def popMax(self) -> int:
        tmp = []
        while self.stack1[-1] != self.stack2[-1]:
            tmp.append(self.stack1.pop())
            self.stack2.pop()
        ret = self.stack1.pop()
        self.stack2.pop()
        for i in tmp[::-1]:
            self.push(i)
        return ret



if __name__ == '__main__':
    stack = MaxStack()
    stack.push(5)
    stack.push(1)
    print(stack.popMax())
    print(stack.popMax())