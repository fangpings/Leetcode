class Solution:
    def findMinDifference(self, timePoints):
        timePoints = [self.convert_to_min(time) for time in timePoints]
        timePoints.sort()
        print(timePoints)
        return min([timePoints[i+1] - timePoints[i] for i in range(len(timePoints) - 1)] + [1440 - timePoints[-1] + timePoints[0]])

    def convert_to_min(self, time):
        hour, minute = time.split(':')
        return int(hour) * 60 + int(minute)

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMinDifference(["19:59","00:00", '12:35']))