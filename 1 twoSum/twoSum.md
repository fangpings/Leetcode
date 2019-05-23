### 1 Two Sum

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

#### 暴力搜索

$O(N^2)$时间复杂度，两层循环即可

#### Hash table

思想：将值转换为Key，将index转换为value，只要查找特定值的complement是否在hash table里面即可

两遍循环，$O(N)$时间复杂度

#### 注意点

1. 题目不允许相同下标作为返回值，即[3,2,4]目标6时不允许返回[0,0]
2. 有可能有相同值，即[3,3]目标6。如果在将数组转换为dict的过程中出现重复key，直接判断该重复key是否符合条件，符合条件直接返回，不符合条件就记录位置即可
3. Hash table实际上只关心Key的位置，Value的位置应该是通过Key的位置来维护的另外一个数组。想象如果Hash table的size和Key的最大size一样大，那么只需要将key本身作为hash值，维护一个数组即可。但是如果Hash table的size小于Key的最大size，那么势必存在key->hash->value, 至少需要两个数组或者一个数组->链表结构。