class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        current_min = self.getMin()
        if current_min == None or x < current_min:
            current_min = x
        self.stack.append((x, current_min))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
        else:
            return None
if __name__ == '__main__':
    s = MinStack()
    s.push(0)
    s.push(1)
    s.push(0)
    print(s.getMin())
    s.pop()
    # print(s.stack)
    print(s.getMin())