import heapq

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [[0, i] for i in range(numCourses)]
        out = [[] for i in range(numCourses)]
        for i, j in prerequisites:
            out[j].append(i)
            indegree[i][0] += 1

        heapq.heapify(indegree)
        print(indegree)
        while indegree:
            degree, index = heapq.heappop(indegree)
            print(indegree)
            if degree != 0:
                return False
            for o in out[index]:
                for i in range(len(indegree)):
                    if indegree[i][1] == o:
                        indegree[i][0] -= 1
            heapq.heapify(indegree)
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(3, [[0,1], [1,0],[1,2]]))