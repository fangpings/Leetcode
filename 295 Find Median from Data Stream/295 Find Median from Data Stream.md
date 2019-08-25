### 295 Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,

```
[2,3,4]`, the median is `3
[2,3]`, the median is `(2 + 3) / 2 = 2.5
```

Design a data structure that supports the following two operations:

- void addNum(int num) - Add a integer number from the data stream to the data structure.
- double findMedian() - Return the median of all elements so far.

 

**Example:**

```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```

 

**Follow up:**

1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?
2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

### 想法

维护两个heap，一个maxheap，一个minheap，maxheap维护所有小于当前median的数，minheap维护所有大于当前median的数。如果当前两堆数量相等，当前median等于minheap的最小值和maxheap的最大值的平均值，否则等于较多的那个堆的最大或者最小值。

要插入的时候，我们先检查当前插入值和当前median的大小。如果大于当前median，那么插入到minheap。如果minheap的数目不大于maxheap的数目，那么直接插入就行，如果minheap的数目比maxheap的数目多1（注意至多只会多1），那么我们先把minheap的最小值pop出来并插入到maxheap，然后再把当前值插入到minheap。

然后一个小技巧，python的heapq只实现了最小堆，那我们需要最大堆怎么办呢。我们可以每次要插入最大堆的时候，都只插入当前元素的相反数，每次要取数的时候也取相反数。

然后对于第一个follow up，我们可以用bucket。注意这和164 Maximum Gap很像。事实上对于所有上下限受限的题目，我们都可以考虑用bucket来缩减复杂度。