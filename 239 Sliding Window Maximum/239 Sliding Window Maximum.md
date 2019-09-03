### 239 Sliding Window Maximum

Given an array *nums*, there is a sliding window of size *k* which is moving from the very left of the array to the very right. You can only see the *k* numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

**Example:**

```
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Note:** 
You may assume *k* is always valid, 1 ≤ k ≤ input array's size for non-empty array.

**Follow up:**
Could you solve it in linear time?

### 想法

1. ![WechatIMG841](/Users/Kururuken/Desktop/Leetcode/239 Sliding Window Maximum/WechatIMG841.jpeg)

   这个方法最大的问题就是题目里面有一句You can only see the *k* numbers in the window，不知道有没有违反，倒是很精妙就是了。

2. 用deque（这个数据结构就是可以两头push两头pop的结构）重要的是我们维护这个deque是递减的结构。我们在deque里面储存元素的index。每次我们当前index前进一步，如果deque[0]储存的index已经out of sliding window了（也有可能是不会out的！），那么把头上pop出去，然后我们开始着手加入这个index，我们不断pop出尾巴上的index，如果尾巴上的index对应的元素小于当前元素（这种元素是永远没有机会成为最大值的）这样我们就不断在维护一个递减的结构。最后每一步我们都把头上的元素作为当前sliding window的最大值。