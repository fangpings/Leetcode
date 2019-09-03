from collections import defaultdict
import heapq
class Solution:
    def getSkyline(self, buildings):
        start_dict = defaultdict(list)
        end_dict = defaultdict(list)
        height_dict = defaultdict(int)
        sequence = []
        for i in range(len(buildings)):
            sequence.append((buildings[i][0], 1))
            sequence.append((buildings[i][1], 0))
            start_dict[buildings[i][0]].append(i)
            end_dict[buildings[i][1]].append(i)
            height_dict[i] = buildings[i][2]
        sequence.sort(key=lambda x: x[0])
        used = [0 for _ in range(len(buildings))] + [0]
        ret = []
        current_heights = [(0, -1)]
        max_height = 0
        for pos, start in sequence:
            if start:
                index = start_dict[pos].pop()
                heapq.heappush(current_heights, (-height_dict[index], index))
                # current_heights.append(height_dict[index])
                # current_heights.sort()
                if -current_heights[0][0] > max_height:
                    max_height = -current_heights[0][0]
                    ret.append([pos, max_height])
            else:
                index = end_dict[pos].pop()
                used[index] = 1
                print(current_heights[0])
                while used[current_heights[0][1]]:
                    heapq.heappop(current_heights)
                # current_heights.remove(height_dict[index])
                # current_heights.sort()
                if -current_heights[0][0] < max_height:
                    max_height = -current_heights[0][0]
                    ret.append([pos, max_height])
        i = 0
        while i + 1 < len(ret):
            if ret[i][0] == ret[i+1][0]:
                if ret[i-1][1] == ret[i+1][1]:
                    ret.pop(i)
                    ret.pop(i)
                else:
                    ret.pop(i)
            else:
                i += 1
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.getSkyline([ [2,9, 10]]))

