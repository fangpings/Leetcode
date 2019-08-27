class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flattened = []
        for i in nestedList:
            self.flattened += self.flatten(i)
        self.cursor = 0

    def flatten(self, nestedList):
        ret = []
        if nestedList.isInteger():
            return nestedList.getInteger()
        for i in nestedList.getList():
            ret += self.flatten(i)
        return ret
        

    def next(self):
        """
        :rtype: int
        """
        self.cursor += 1
        return self.flattened[self.cursor-1]


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cursor == len(self.flattened)
