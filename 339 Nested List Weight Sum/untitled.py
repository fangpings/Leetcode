class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.ret = 0
        self.rec(nestedList, 1)
        return self.ret
    
    def rec(self, nl, dep):
        for i in nl:
            if i.isInteger():
                self.ret += dep * i.getInteger()
            else:
                self.rec(i.getList(), dep + 1)
                