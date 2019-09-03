"""
# Definition for an Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule):
        worktime = []
        for s in schedule:
            worktime = self.merge(worktime, s)
            print(worktime)
        ret = []
        for i in range(len(worktime) - 1):
            ret.append([worktime[i][1], worktime[i+1][0]])
        return ret

    def merge(self, time1, time2):
        if not time1:
            return time2
        if not time2:
            return time1
        cur1, cur2 = 0, 0
        ret = []
        while cur1 < len(time1) and cur2 < len(time2):
            item1, item2 = time1[cur1], time2[cur2]
            if item1[0] <= item2[0]:
                if not ret:
                    ret.append(item1)
                else:
                    if item1[0] <= ret[-1][1]:
                        if item1[1] > ret[-1][1]:
                            ret[-1][1] = item1[1]
                    else:
                        ret.append(item1)
                cur1 += 1
            else:
                if not ret:
                    ret.append(item2)
                else:
                    if item2[0] <= ret[-1][1]:
                        if item2[1] > ret[-1][1]:
                            ret[-1][1] = item2[1]
                    else:
                        ret.append(item2)
                cur2 += 1
        while cur2 < len(time2):
            item2 = time2[cur2]
            if item2[0] <= ret[-1][1]:
                if item2[1] > ret[-1][1]:
                    ret[-1][1] = item2[1]
            else:
                ret.append(item2)
            cur2 += 1
        while cur1 < len(time1):
            item1 = time1[cur1]
            if item1[0] <= ret[-1][1]:
                if item1[1] > ret[-1][1]:
                    ret[-1][1] = item1[1]
            else:
                ret.append(item1)
            cur1 += 1
        return ret



if __name__ == '__main__':
    sol = Solution()
    print(sol.employeeFreeTime([[[1,2]],[[2,10]],[[1,2]],[[5,10]]]))
