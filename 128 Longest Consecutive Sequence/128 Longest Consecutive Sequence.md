### 128 Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(*n*) complexity.

**Example:**

```
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### 想法

#### 排序

先排序，然后顺序找下来判断就行了。时间复杂度O(NlogN)。

#### Hashset

核心思想是每碰到一个在set里面的数，**我们直接对它不断+1，判断他的后继们是否在set里面**。Hashset判断某个元素是否存在应当是平均O(1)的算法。所以这个应该是平均O(N)的算法。

```python
class Solution:
    def longestConsecutive(self, nums):
        mapping = set(nums)
        longest = 0
        for num in mapping:
            if num - 1 not in mapping:  # 这一步判断这个元素是否是某一段Consecutive的中间元素
                current_num = num
                current = 1

                while current_num + 1 in mapping:
                    current_num += 1
                    current += 1

                if current > longest:
                    longest = current
        return longest
```

Python的set应该就是Hashset的实现，查找某元素是否在里面只需要O(1)