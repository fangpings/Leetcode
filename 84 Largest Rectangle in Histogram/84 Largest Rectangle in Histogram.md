### 84 Largest Rectangle in Histogram

Given *n* non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram. 

![img](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)
Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.

 

![img](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)
The largest rectangle is shown in the shaded area, which has area = `10` unit.

**Example:**

```
Input: [2,1,5,6,2,3]
Output: 10
```

#### 想法

1. 这个是我自己想的，但是没过time。。

   递归地找面积最大值，每次找到当前序列最小值，乘上当前序列长度作为当前候选值，然后以最小值去split这个序列。对每个subhistogram，我们重复这个操作，当序列长度为1的时候直接返回高度。从当前候选和所有subhitogram的最大值里面选出最大值。

   这个解法最大的问题就是最小值不好找。平均和最差Time Complexity肯定是都是O(N^2)

2. 这个是别人的，绝了。。

   ```python
   class Solution:
       def largestRectangleArea(self, heights):
           heights.append(0)
           stack = [-1]
           ret = 0
           for i in range(len(heights)):
               while heights[i] < heights[stack[-1]]:
                   h = heights[stack.pop()]
                   w = i - stack[-1] - 1
                   ret = max(ret, h * w)
               stack.append(i)
           return ret
   ```

   这个解法里面我们对于递增的block一律先不管，只是把block的index加入我们的stack里面。等到到了某一个位置的block高度减了，我们开始计算(全递增也不要紧，第一行在heights的最后append了一个0)。计算过程是这样的，长方形的高度为`heights[stack.pop()]`,即栈顶代表的index的高度，宽度的右边很明显就是i（i本身不包括）,因为i-1的高度是比i高的，宽度的左边应当是左边第一个比栈顶代表的index的高度低的位置。如果左边没有比他高的位置了，那左边就取-1，(stack一开始就有-1这个值有两个作用(这怎么想到的。。)，一个是和高度最后的0对应，一个就是左边界一直有一个-1)。我们要明确的就是**`stack[-1]`代表比当前计算block()的高度还要低的左边第一个block的位置**，这样我们就保证了我们计算的正确性。

   我们举三个例子来看一下

   1. `[1,2,3]`

      这个就是纯递增的例子。while block一直不会执行，直到最后我们统一计算。这个时候i=3，第一个出栈的是index=2，height=3，他的宽度只有1(因为**到i=3距离**只有1)。下一个出栈的是index=1，height=2，他的宽度有2，面积为4最大，下一个出栈的是index=0， height=1，他的宽度有3.

   2. `[3,2,1]`

      这个是一个纯递减例子。纯递减的时候每次栈里面只会有两个元素，每次进一个元素就会直接出去。第一次进index=0， height=3，第二次的时候因为2<3，栈顶出栈，计算宽度为当前位置到开始位置-1。然后进index=1，height=2。下次出栈的时候计算宽度会增加，因为左边界一直都是-1

   3. [2,3,5,6,4]

      这个例子在到4之前全是递增的，只做入栈操作。到了4之后，我们首先计算5，6。这两个计算完了之后我们发现4比3大了，我们把4入栈，然后到头了，我们再计算。这个时候不再是连续的index了，但是递增性没有改变。**而且中间的出栈的元素肯定比当前栈中的所有元素都要大，我们可以放心直接算到stack顶的index。**这个例子也可以说明while的判断条件的理由。5和6的右边不能再加入4，因为5和6比4高，要拼长方形高度应当用4.而2，3比4低，拼长方形的时候高度和4无关。