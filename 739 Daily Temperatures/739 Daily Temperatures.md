### 739 Daily Temperatures

Given a list of daily temperatures `T`, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put `0` instead.

For example, given the list of temperatures `T = [73, 74, 75, 71, 69, 72, 76, 73]`, your output should be `[1, 1, 4, 2, 1, 1, 0, 0]`.

**Note:** The length of `temperatures` will be in the range `[1, 30000]`. Each temperature will be an integer in the range `[30, 100]`.

### 想法

翻译一下就是找数组某个位置后面过几位有第一个比当前位置大的数，注意到温度是有上限的，于是我们考虑可以用hashmap储存每个位置的温度和对应index，然后我们从右往左遍历数组，每次都从当前温度一度一度往上找，找到最近的index(注意这个是一定要遍历到最后的),其实时间复杂度也是O(N）哦

当然也有更方便的做法，又是用stack（我发现用一个stack来回pop的题目都很牛逼，下次有机会整理一下）

我们从右往左遍历数组，对于当前元素，我们检查栈顶元素（栈储存的是index),如果栈顶元素对应温度比当前温度低，那我们把他pop出去

![1](/Users/Kururuken/Desktop/Leetcode/739 Daily Temperatures/1.jpeg)

我们观察到如果我们需要这样一个递增子序列的结构来实现我们的目的，那stack是非常管用的，应该立刻想到。

类似的题目还有654 Maximum Binary Tree 和 84 Largest Rectangle in Histogram(这题算是维护一个递减的结构，不过差不多)