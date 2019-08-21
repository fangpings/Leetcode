class Solution:
    def kClosest(self, points, K):
        if K == 0:
            return []
        self.points = points
        self.select_k(0, len(points) - 1, K)
        return self.points[:K]

    def select_k(self, i, j, k):
        if i >= j:
            return
        mid = (i + j) // 2
        self.points[i], self.points[mid] = self.points[mid], self.points[i]
        dist = lambda x: x[0] ** 2 + x[1] ** 2
        anchor = dist(self.points[i])
        oi = i
        oj = j
        i += 1
        while i < j:
            while i < j and dist(self.points[i]) <= anchor:
                i += 1
            while i < j and dist(self.points[j]) > anchor:
                j -= 1
            self.points[i], self.points[j] = self.points[j], self.points[i]
        if dist(self.points[i]) < anchor:
            self.points[i], self.points[oi] = self.points[oi], self.points[i]
        if j - oi < k:
            self.select_k(j, oj, k - (j - oi))
        elif j - oi > k:
            self.select_k(oi, j, k)

if __name__ == '__main__':
    sol = Solution()
    print(sol.kClosest([[1,3],[-2,2],[2,-2]], 2))

