### 201 Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

**Example 1:**

```
Input: [5,7]
Output: 4
```

**Example 2:**

```
Input: [0,1]
Output: 0
```

###  想法

可以发现，**如果两个二进制数的最高第k位不相同，那么对以这两个数为范围内的所有数取AND，右边k位肯定为全0**。这是因为如果右边第i位两个数不相同，那么取AND已经为0，如果两个数相同，但是因为上面位置的数仍然有不相同的，所以在这中间的某个数的第i位一定也为0，那么取AND还是为0.

所以我们只需要不断对m，n右移，直到m，n相等。这个时候m，n剩下的位数是不会变了，意味着位于m，n中间的所有数，最高的剩下位数也和现在的m，n相同。然后我们记录m，n右移了多少位，再左移回去就可以了

