### 75 Sort Colors

Given an array with *n* objects colored red, white or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

**Note:** You are not suppose to use the library's sort function for this problem.

**Example:**

```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Follow up:**

- A rather straight forward solution is a two-pass algorithm using counting sort.
  First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
- Could you come up with a one-pass algorithm using only constant space?

#### 想法

1. 先说一个看上去非常聪明的方法，虽然不快

   ```python
   def sortColors(self, nums):
       i = j = 0
       for k in range(len(nums)):
           v = nums[k]
           nums[k] = 2
           if v < 2:
               nums[j] = 1
               j += 1
           if v == 0:
               nums[i] = 0
               i += 1
   ```

   这个方法巧妙地把整个数组分成了三块0，1，2。首先我们默认整个数组全部都是2，然后我们判断当前这个数到底是几(这里注意一定要先把当前数组的数保存下来，然后修改成2)。如果是1，那我们把1的边界上(`j`)的值修改成1，然后拓展1的边界(`j += 1`)，最后我们在判断是不是0，如果是0，那么我们最后把0(`i`)边界上的值修改成0，然后拓展0的边界。巧妙之处在于我们没有用`elif`，而是顺序判断下来，这样如果需要拓展0的边界，那么势必1的边界也会随之拓展。

   但是缺点是很多操作是多余的，这个不凑巧一次循环要操作3次。而count sort相当于一次循环做两次操作而已。

2. 再说一个更快一点的

   ```python
   class Solution:
       def sortColors(self, nums):
           """
           Do not return anything, modify nums in-place instead.
           """
           l, r = 0, len(nums) - 1
           i = 0
           while i <= r:
               if nums[i] == 2 and i < r:
                   nums[i], nums[r] = nums[r], nums[i]
                   r -= 1
               elif nums[i] == 0 and i > l:
                   nums[i], nums[l] = nums[l], nums[i]
                   l += 1
               else:
                   i += 1
   ```

   这个算法是维护0和2的边界。如果当前值是2，那么就和2边界上的值交换，0也一样，1不动，当前位置向前推进。

   注意这几个细节：

   1. 循环的条件是`i <= r`即可，i到达2的边界后没必要再继续了，但是这个等号一定要取到，因为r实际上是表示r边界外的第一点，如果不取到等号那么相当于有一个点没有判断了 
   2. 如果要交换，那么i是不动的，因为你不知道换回来的是什么东西,有可能还是2换回来的还是2，但是边界是确定会变动的，因为换到边界上的东西是确定的 
   3. 判断里面`i < r`和`i > l`这两条是非常重要的，因为有时候换完i是不会动的，我们要确保所有`< l`或者`> r`的东西都是已经正确的，如果i在这两个范围之内，那么我们这个时候绝对不能动。注意这两个边界条件取不取等式无所谓的，去取等相当于原地换，没意义