class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x:x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.canAttendMeetings([[7,10]]))
