### 973 K Closest Points to Origin

We have a list of `points` on the plane.  Find the `K` closest points to the origin `(0, 0)`.

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

**Example 1:**

```
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
```

**Example 2:**

```
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
```

 

**Note:**

1. `1 <= K <= points.length <= 10000`
2. `-10000 < points[i][0] < 10000`
3. `-10000 < points[i][1] < 10000`

### 想法

一个办法是直接对距离排序，这个很trivial。

注意到题目**只要求取前K个最近的，而对顺序没有任何要求**。所以我们可以采用类似于快速选择的算法。即我们随机选择一个pivot元素，然后把pivot元素和头上的元素进行交换，接下俩对剩下的元素一头一尾，左边的必须<=pivot元素，右边的必须>pivot元素，把左右不符合的元素交换位置，直到左右两个指针相等。这个时候如果指向的元素小于pivot元素，那么用当前元素和pivot元素交换，如果大于等于就不换。

这样我们保证了pivot左边的元素都小于pivot，右边的元素都大于pivot。然后我们比较pivot的位置和K的大小，如果刚好等于pivot说明我们找到了K个最小的元素，如果小于K，说明只能保证前pivot位置个元素是最小的，那么我们在剩下的数组里面重新找k-pivot个，如果大于K，那说明找多了，但是我们可以缩小找的范围，即在0，pivot这个范围里面重新找K个。

里面的大于号小于号都是很tricky的，一个不小心就会弄错。。

```python
class Solution:
    def kClosest(self, points, K):
        if K == 0:
            return []
        self.points = points
        self.select_k(0, len(points) - 1, K)
        return self.points[:K]

    def select_k(self, i, j, k):
        if i >= j: # 这里必须是大于等于，因为下面结束循环的条件就是i=j
            return
        mid = (i + j) // 2
        self.points[i], self.points[mid] = self.points[mid], self.points[i]
        dist = lambda x: x[0] ** 2 + x[1] ** 2
        anchor = dist(self.points[i])
        oi = i
        oj = j
        i += 1
        while i < j: # 如果把循环条件设成i<=j,那么最后就会出现i>j的情况，更麻烦
            while i < j and dist(self.points[i]) <= anchor: # 要在这里就判断i会不会大于j
                i += 1
            while i < j and dist(self.points[j]) > anchor:
                j -= 1
            self.points[i], self.points[j] = self.points[j], self.points[i]
        if dist(self.points[i]) < anchor: #这里一定要做判断，因为有时候需要换，有时候不需要换
            self.points[i], self.points[oi] = self.points[oi], self.points[i]
        if j - oi < k:
            self.select_k(j, oj, k - (j - oi))
        elif j - oi > k:
            self.select_k(oi, j, k)
```

