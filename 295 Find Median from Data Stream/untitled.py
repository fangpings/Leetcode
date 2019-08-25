import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        self.median = None

    def addNum(self, num: int) -> None:
        if not self.minheap and not self.maxheap:
            self.minheap.append(num)
            self.median = float(num)
        else:
            if num > self.median:
                if len(self.minheap) > len(self.maxheap):
                    tmp = heapq.heapreplace(self.minheap, num)
                    heapq.heappush(self.maxheap, -tmp)
                else:
                    heapq.heappush(self.minheap, num)
            else:
                if len(self.maxheap) > len(self.minheap):
                    tmp = -heapq.heapreplace(self.maxheap, -num)
                    heapq.heappush(self.minheap, tmp)
                else:
                    heapq.heappush(self.maxheap, -num)
            if len(self.minheap) == len(self.maxheap):
                self.median = (self.minheap[0] - self.maxheap[0]) / 2
            elif len(self.minheap) < len(self.maxheap):
                self.median = float(-self.maxheap[0])
            else:
                self.median = float(self.minheap[0])

    def findMedian(self) -> float:
        return self.median


if __name__ == '__main__':
    m = MedianFinder()
    m.addNum(40)
    m.addNum(12)
    print(m.findMedian())
    m.addNum(16)
    print(m.findMedian())
    m.addNum(14)
    print(m.findMedian())


