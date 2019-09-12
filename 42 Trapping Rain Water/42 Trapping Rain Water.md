### 42 Trapping Rain Water

Given *n* non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![img](https://ws2.sinaimg.cn/large/006tNc79ly1g1qyybq423j30bg04hmx3.jpg)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. 

#### 想法

### 慢

我们先不找蓝色面积。我们考虑用大长方形面积$S=h_{max}*len(h)$减去白色面积再减去黑色面积。黑色面积可由`heights`全部相加得到。我们考虑白色面积的计算（白色面积可由$O(N)$得到）。

首先我们找到最高的`h`，如果有重复的最高的，取最左和最右的坐标`left`和`right`，对于所有`i < left`，我们找到次最高值`left_max`和它的坐标`left_max_index`，我们这一层左半部分的白色部分面积可由`left * (height[left] - left_max)`得到，右半部分同理。然后我们令`left = left_max_index, right = right_max_index`，重复，直到抵达数组两头。

### 较快

对于一个位置i，他能装的水的量为

```
max(min(height[:i+1], height[i:]) - height[i], 0)
```

即左边所有的最大值（包括自己）和右边所有的最大值（包括自己的）较小值减掉自身的高度

对于每个位置都重新找太慢了，可以从左往右遍历一遍找到所有位置的左边的最大值，然后再从右往左遍历一遍找到所有位置的右边的最大值，然后对于每个位置再利用上面的方法去算能装水的量。

