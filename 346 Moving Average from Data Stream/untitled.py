from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.deque = deque()
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.deque) < self.size:
            self.deque.appendleft(val)
            self.sum += val
            return self.sum / len(self.deque)
        else:
            self.sum -= self.deque.pop()
            return self.next(val)

            