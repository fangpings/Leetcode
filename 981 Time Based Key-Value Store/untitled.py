from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = defaultdict(list)       

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        data = self.hashmap[key]
        if not data or timestamp < data[0][1]:
            return ''
        l, r = 0, len(data) - 1
        while l < r:
            mid = (l + r) // 2
            if data[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if data[l][1] <= timestamp:
            return data[l][0]
        else:
            return data[l-1][0]