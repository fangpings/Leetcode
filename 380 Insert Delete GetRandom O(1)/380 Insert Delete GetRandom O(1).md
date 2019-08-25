### 380 Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in *average* **O(1)**time.

1. `insert(val)`: Inserts an item val to the set if not already present.
2. `remove(val)`: Removes an item val from the set if present.
3. `getRandom`: Returns a random element from current set of elements. Each element must have the **same probability** of being returned.



**Example:**

```
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
```

### 想法

相当于要做到四个O(1)：维护所有元素的list，增加，删除，查找。

我们考虑用一个hashmap做到O(1)的增加删除查找，但是hashmap的一个严重的问题是如果要在所有元素里面随机选一个，**它总是要遍历所有key的，所以第一项做不到O(1)**。那么我们考虑再增加一个list，这样我们相当于以O(1)返回所有元素，再在里面随机选择一个就可以了。**但是list的查找和删除是做不到同时O(1)的**，因为要不然我们记录每个元素的位置，这样查找可以是O(1)，但是删除就要更新所有元素的位置就变成O(N)了。

这里就有一个非常聪明的想法了，我们的hashmap记录每个元素在list中的位置，这样除了删除都是O(1),删除的时候，**我们把最后一个元素填入待删除元素的slot里面，这样我们只需要更新一个元素的新位置就可以了。**