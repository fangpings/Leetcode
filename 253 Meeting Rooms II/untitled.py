class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        rooms = []
        for meeting in intervals:
            flag = False
            for room in rooms:
                if meeting[0] >= room[-1][1]:
                    room.append(meeting)
                    flag = True
                    break
            if not flag:
                rooms.append([meeting])
        return len(rooms)

if __name__ == '__main__':
    sol = Solution()
    print(sol.minMeetingRooms([[13,15],[1,13]]))



