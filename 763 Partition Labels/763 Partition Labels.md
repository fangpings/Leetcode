### 763 Partition Labels

A string `S` of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

**Example 1:**

```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

**Note:**

1. `S` will have length in range `[1, 500]`.
2. `S` will consist of lowercase letters (`'a'` to `'z'`) only.

### 想法

1. 把每个字符的起始位置和结束位置记下来，然后根据起始位置排序，接下来就是merge interval了，如果两个interval有交叉，那就合并，否则就保留，这样保证各个interval不相交这个最差情况是O(NlogN)

2. 另一个办法是这样的

   ```python
   class Solution(object):
       def partitionLabels(self, S):
           last = {c: i for i, c in enumerate(S)}
           j = anchor = 0
           ans = []
           for i, c in enumerate(S):
               j = max(j, last[c])
               if i == j:
                   ans.append(i - anchor + 1)
                   anchor = i + 1
               
           return ans
   ```

   只记录每个字符最后出现的位置，然后用三个指针，一个指向上一个interval结束的位置（或者当前interval开始的位置），第二个指向当前interval最远的位置（这个每次都和当前字符最后出现的位置比较并更新），第三个指向当前位置，如果当前位置和interval最远的位置重合了，就说明当前interval结束了。

