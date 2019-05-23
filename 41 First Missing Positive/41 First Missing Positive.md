### 41 First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

**Example 1:**

```
Input: [1,2,0]
Output: 3
```

**Example 2:**

```
Input: [3,4,-1,1]
Output: 2
```

**Example 3:**

```
Input: [7,8,9,11,12]
Output: 1
```

**Note:**

Your algorithm should run in *O*(*n*) time and uses constant extra space.

#### 想法

这题好难。自己没做出来，贴一下别人的代码

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        l = len(nums)
        for i in range(l):
            if nums[i] < 0 or nums[i] >= l:
                nums[i] = 0
        for i in range(l):
            nums[nums[i] % l] += l
        for i in range(1, l):
            if nums[i]//l == 0:
                return i
        return l
```

首先有几点: **1. constant extra space注意extra，我们可以在原数组上修改 2. O(n)时间，但是我们可以跑很多遍循环**

再讲一讲想法：对于长度是k的数组，我们的答案只可能在[1, 2, …, k+1]里面选。这启发了我们，我们可以**把原数组变成一个长度为k+1的hashtable，hash函数直接对k+1取模就可以了**，具体来说我们首先在最末尾插入一个0把数组变成k+1的长度(0不会影响结果，插入的原因是我们要给k+1 mod 0的数一个位置，虽然这些数不会参与我们之后的计算)

然后我们对所有小于0的数或者>=k+1的数，直接把他们变成0，因为他们不影响我们的结果。**注意这步之后我们的数组里面只有[0, k]范围内的数了。**

然后是关键的一步，我们对每个元素`nums[nums[i] % l] += l`，[0, k]范围内的数对k+1取模，答案刚好落在[0, k]的index里面，我们现在的数组长度刚好容纳这些数。对每个位置，我们都加k+1的原因是我们要在保留原数组信息的同时对数组修改，**而加上k+1不会影响取模的值，也就是说前面位置对后面位置的变动不会影响后面位置自身的信息**，然后我们找到第一个除k+1的商为0的值(注意这里不能写成`nums[i] == 0`,因为**这个时候我们已经不关心原数组的值了，我们只需要知道`nums[i]//l`的值，这代表了`i`出现的次数**，我们找到最小的出现次数是0的`i`就可以了

**这题的想法太精妙了**