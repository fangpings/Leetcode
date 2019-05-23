### 55 Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

**Example 1:**

```
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
```

#### 想法

一开始用了和Jump Game II一样的思路，从头开始找。但是做完居然只有28%

其实不找最短，只看能不能到的话，我一开始的思路倒着找是可以的

```c++
bool canJump(int A[], int n) {
    int last=n-1,i,j;
    for(i=n-2;i>=0;i--){
        if(i+A[i]>=last)last=i;
    }
    return last<=0;
}
```

我们倒着找哪个点能到达last之后，如果能到达，我们继续找前面的哪个点能到达这个点。如果最后的点不是起点，说明起点到不了终点。