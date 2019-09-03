### 218 The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are **given the locations and height of all the buildings** as shown on a cityscape photo (Figure A), write a program to **output the skyline** formed by these buildings collectively (Figure B).

[![Buildings](https://assets.leetcode.com/uploads/2018/10/22/skyline1.png) ](https://leetcode.com/static/images/problemset/skyline1.jpg)

For instance, the dimensions of all buildings in Figure A are recorded as: `[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] `.

The output is a list of "**key points**" (red dots in Figure B) in the format of `[ [x1,y1], [x2, y2], [x3, y3], ... ]` that uniquely defines a skyline. **A key point is the left endpoint of a horizontal line segment**. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:`[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]`.

**Notes:**

- The number of buildings in any input list is guaranteed to be in the range `[0, 10000]`.
- The input list is already sorted in ascending order by the left x position `Li`.
- The output list must be sorted by the x position.
- There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `[...[2 3], [4 5], [7 5], [11 5], [12 7]...]` is not acceptable; the three lines of height 5 should be merged into one in the final output as such: `[...[2 3], [4 5], [12 7], ...]`

### 想法

这个skyline contour的key point只会出现在每栋楼开始和结束的地方，所以我们先把所有的楼的开始和结束的位置拉平，然后sort，在这个数组里我们记录这个位置是楼的开始还是楼的结束。然后我们遍历这个数组

现在key point只会有两种情况，第一是现在是一栋楼的start，并且这栋楼的height大于当前的height，第二是现在是当前height楼的结束，那么我们需要找到当前第二高的楼的height。

第一种情况是好解决的，难点在于第二种情况。第二种情况的复杂之处在于我们如果使用heap来寻找最高height，那么问题就是如果碰到了当前楼结束，但是当前楼的高度不是最高的height，那么我们应该怎么去维护这个heap呢？**即heap的非最大最小元素要怎么出去呢？**

**一个非常聪明的解决方案是lazy delete，即我们维护一个used[]数组，每当一个楼结束，我们只在used[]数组里面标记，而每次我们需要最大值的时候，我们都反复pop直到当前的最大值归属的楼不再是used。**这个想法在716 Max Stack中也有体现。 Lazy delete是一个值得学的技巧。