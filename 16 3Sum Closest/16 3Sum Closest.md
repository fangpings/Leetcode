### 16 3Sum Closest

Given an array `nums` of *n* integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

**Example:**

```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

#### 想法

一开始的想法和3Sum类似，前两个数做循环，由于第三个数不能再直接用HashMap得到，考虑先给整个数组做排序再用二分查找最接近的数，这样的复杂度是$O(N^2\log{N})$.但是实际上挺慢的，可能是编码的细节问题

#### 改进

```python
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result
```

我没什么好说的，这我也不知道该怎么想。**总之一句话，先排序之后再分别从两头向中间靠近，这个思路应该能解决一些问题**