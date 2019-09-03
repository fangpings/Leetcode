import heapq
from collections import defaultdict

# class Solution:
#     def leastInterval(self, tasks, n):
#         tasks_num = defaultdict(int)
#         for t in tasks:
#             tasks_num[t] += 1
#         ready = []
#         for t, num in tasks_num.items():
#             ready.append((-num, t))
#         heapq.heapify(ready)
#         cool_down = ['idle' for _ in range(n)]
#         ret = []
#         total = len(tasks)
#         while total > 0:
#             if not ready:
#                 cool_down.append('idle')
#                 ret.append('idle')
#             else:
#                 next_task = heapq.heappop(ready)[1]
#                 tasks_num[next_task] -= 1
#                 if tasks_num[next_task]:
#                     cool_down.append(next_task)
#                 else:
#                     cool_down.append('idle')
#                 ret.append(next_task)
#                 total -= 1
#             if cool_down:
#                 next_ready = cool_down.pop(0)
#                 if next_ready != 'idle':
#                     heapq.heappush(ready, (-tasks_num[next_ready], next_ready))
#         return len(ret)

class Solution:
    def leastInterval(self, tasks, n):
        count = [0 for _ in range(26)]
        max_freq = 0
        max_count = 0
        for t in tasks:
            count[ord(t) - ord('A')] += 1
            if count[ord(t) - ord('A')] > max_freq:
                max_freq = count[ord(t) - ord('A')]
                max_count = 1
            elif count[ord(t) - ord('A')] == max_freq:
                max_count += 1

        sections = max_freq - 1
        sections_length = max(n+1, max_count)
        return max(len(tasks), sections * sections_length + max_count)

if __name__ == '__main__':
    sol = Solution()
    print(sol.leastInterval(["A","A","A","B","B","B"], 2))



