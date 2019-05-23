### 93 Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

**Example:**

```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

#### 想法

本质上还是和91 Decode Ways的想法一样用DP

但是这题要复杂不少。要考虑以下几个问题：

1. '.'的出现次数，即最多只能有四段分隔
2. 0是不能在同一段分隔里面连续出现的， 即00.00这种是不行的
3. 在向后查看dp数组的时候要考虑+1, +2会不会越过dp数组的界
4. 一组分隔最大只能到255