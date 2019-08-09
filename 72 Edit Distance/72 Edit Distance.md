### 72 Edit Distance

Given two words *word1* and *word2*, find the minimum number of operations required to convert *word1* to *word2*.

You have the following 3 operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

**Example 1:**

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

**Example 2:**

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

想法

假设，a 的长度是 m，b 的长度是 n，要求 a[1]a[2]...a[m] => b[1]b[2]...b[n] 的最小编辑距离，记为 d[m][n]。

1. 如果 a[m] === b[n]，那么问题转化为求解：a[1]a[2]...a[m-1] => b[1]b[2]...b[n-1] 的最小编辑距离，因此 d[m][n] === d[m-1][n-1]。比如，"xyz" => "pqz" 的最小编辑距离等于 "xy" => "pq" 的最小编辑距离。
2. 如果 a[m] !== b[n]，又分为三种情况：
   1. 比如，"xyz" => "efg" 的最小编辑距离等于 "xy" => "efg" 的最小编辑距离 + 1（因为允许插入操作，插入一个 "z"），抽象的描述便是 `d[m][n]=== d[m-1][n] + 1`。
   2. 比如，"xyz" => "efg" 的最小编辑距离等于 "xyzg" => "efg" 的最小编辑距离 + 1，且因为最后一个字符都是 "g"，根据第一个判断条件，可以再等于 "xyz" => "ef" 的最小编辑距离 + 1，因此，得到结论："xyz" => "efg" 的最小编辑距离等于 "xyz" => "ef" 的最小编辑距离 + 1，抽象的描述便是：``d[m][n] === d[m][n-1] + 1`。
   3. 比如，"xyz" => "efg" 的最小编辑距离等于 "xyg" => "efg" 的最小编辑距离 + 1（因为允许替换操作，可以把 "g" 换成 "z"），再等于 "xy" => "ef" 的编辑距离 + 1（根据第一个判断条件），抽象的描述便是： `d[m][n] === d[m-1][n-1] + 1`。
   4. 上述三种情况都有可能出现，因此，取其中的最小值便是整体上的最小编辑距离。
3. 如果 a 的长度为 0，那么 a => b 的最小编辑距离为 b 的长度；反过来，如果 b 的长度为 0，那么 a => b 的最小编辑距离为 a 的长度。