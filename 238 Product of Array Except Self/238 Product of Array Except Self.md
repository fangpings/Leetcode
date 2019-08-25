### 238 Product of Array Except Self

Given an array `nums` of *n* integers where *n* > 1,  return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

**Example:**

```

```

**Note:** Please solve it **without division** and in O(*n*).

**Follow up:**
Could you solve it with constant space complexity? (The output array **does not**count as extra space for the purpose of space complexity analysis.)

### 想法

这题是真的搞，还不准用乘法。。这谁想得到

![img](https://leetcode.com/problems/Figures/238/diag-1.png)

我们发现每个位置的乘积等于他左边的乘积乘他右边的乘积。于是我们可以记录每个位置它左边的乘积，把它放到返回的数组里面。然后我们从右边开始一路乘回来（这个时候不需要额外数组了，只需要一个数来不断记录连续乘积就可以了）

解释起来很麻烦，直接看代码就很方便

```python
class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return []
        product = 1
        ret = []
        for i in nums:
            product *= i
            ret.append(product)
        product = 1
        for i in range(len(nums) - 1, 0, -1):
            ret[i] = ret[i-1] * product
            product *= nums[i]
        ret[0] = product
        return ret
```

