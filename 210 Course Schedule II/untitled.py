class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0 for i in range(numCourses)]
        hashMap = collections.defaultdict(list)
        
        for course, preq in prerequisites:
            hashMap[preq].append(course)
            inDegree[course] += 1
            
        queue = []
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
                
        visited = []
        
        while queue:
            preq = queue.pop()
            visited.append(preq)
            for course in hashMap[preq]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)
        if len(visited) == numCourses:
            return visited
        else:
            return []
            