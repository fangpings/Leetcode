class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x:x.start)
        cur_start = 0
        l = len(intervals)
        ret = []
        while cur_start < l:
            tmp = Interval(intervals[cur_start].start)
            tmp_end = intervals[cur_start].end
            while cur_start + 1 < l and tmp_end >= intervals[cur_start+1].start:
                tmp_end = max(tmp_end, intervals[cur_start+1].end)
                cur_start += 1
            tmp.end = tmp_end
            ret.append(tmp)
            cur_start += 1
        return ret

if __name__ == '__main__':
    start = [Interval(1, 4)]
    sol = Solution()
    end = sol.merge(start)
    print(end)
    for i in end:
        print(i.start, i.end)
