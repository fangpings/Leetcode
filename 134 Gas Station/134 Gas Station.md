### 134 Gas Station

There are *N* gas stations along a circular route, where the amount of gas at station *i* is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from station *i* to its next station (*i*+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

**Note:**

- If there exists a solution, it is guaranteed to be unique.
- Both input arrays are non-empty and have the same length.
- Each element in the input arrays is a non-negative integer.

**Example 1:**

```
Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```

**Example 2:**

```
Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```

#### 想法

还是直接看code来得更快一点。这题可以抽象成一个圆上有一串数，找到一个起始点使得这个位置开始每次向顺时针求和，每个位置的累计和均大于0.

```python
class Solution:
    def canCompleteCircuit(self, gas, cost):
        total = 0
        index = 0
        current_sum = 0
        for i in range(len(gas)):
            current_sum += gas[i] - cost[i]
            if current_sum < 0:
                total += current_sum
                current_sum = 0
                index = i + 1
        total += current_sum
        return index if total >= 0 else -1
```

计算从上个开始位置`i`开始的连续和，如果到了某个点`j`连续和`current_sum`小于0了，说明从`i`到`j`作为开始位置都是不行的。那么我们把`j + 1`定为下一个潜在的开始位置，重复这个操作。在我们不断向右走的同时，我们也保存了左边的连续和的总和，这样当我们遍历完数组的时候，如果某个位置`k`一直向右走到头是可行的，我们再把这个位置到最右的连续和和这个位置左边的连续做个比较，如果这两部分的和还是大于0的那说明这个位置是可以走通的。

对于最后一句话，有两个问题。一个是`k`位置如果向右的连续和大于0，那保不准某个大于`k`的位置向右的连续和也大于0，为什么我们只关注`k`位置呢？第二个问题是假设`k`位置向右能走到头，那为什么`k`位置左边的连续和和右边的连续和之和大于0就能走通？万一出现左边最左是个很大的负数，然后右边跟着一串正数的情况怎么办？

对于第一个问题，一个解释是题目保证了只存在一个unique的解，如果`k`位置可行，那么后面的位置一定不可行，如果`k`位置不可行，那么一定会被移动到下一个可行的位置，不会有遗漏。对于第二个问题我们假设在小于`k`的`i`位置出现了一个很大的负数使得大于`k`的连续和`sum_[k] < diff[i]`,但是我们知道这一点就是`k`被选为备选index的条件就是在`k`这个位置我们的向左连续和大于零了，这个条件已经保证我们不依靠大于`k`的那些位置也可以摆平左边的那些位置（除非是`[-1, -2, -3, 7]`这种最后一位才走通的，这个需要倒数第二句来判断。）