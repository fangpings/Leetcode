### 146 LRU Cache

Design and implement a data structure for [Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU). It should support the following operations: `get` and `put`.

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
`put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a **positive** capacity.

**Follow up:**
Could you do both operations in **O(1)** time complexity?

**Example:**

```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

### 想法

其实最头痛的是怎么维护一个时间性。虽然说我们真正需要的只是least recent的元素，但是还是需要对整体的时间性做一个维护。使用数组是肯定不行的。**数组有这么一个问题，要么查找的时间超过O(1)，要么修改的时间超过O(1)**。我们如果希望修改的时间不超过O(1)的话，一个想法就是使用**双向链表**。链表最大的问题就是查找超过O(1)，**但是我们可以用hashtable去配合链表**使得查找时间也到O(1)。最方便的做法就是key和node对应。这样我们查找和修改的时间均是O(1)了。

另外有一个不容易注意到的小问题是如果插入的key已经存在了，应该是做update而不是直接跳过。