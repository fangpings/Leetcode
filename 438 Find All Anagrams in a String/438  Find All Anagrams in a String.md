### 438  Find All Anagrams in a String

Given a string **s** and a **non-empty** string **p**, find all the start indices of **p**'s anagrams in **s**.

Strings consists of lowercase English letters only and the length of both strings **s**and **p** will not be larger than 20,100.

The order of output does not matter.

**Example 1:**

```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

**Example 2:**

```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

### 想法

差不多就是维护两个hashmap，一个是p的character和count，另一个是当前sliding window的character和count。这里值得注意的一点是，**因为hashmap的key只可能是26个字母，所以我们直接用长度为26的数组代替dict了**。这样比较两个hashmap是否相等也可以直接比较，比用dict不知道方便到哪里去（以后请记得如果只用字符做key，不要再用dict了）

别人写的干净代码贴在这里

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        table = dict(zip('abcdefghijklmnopqrstuvwxyz', range(26)))
        
        tokens = [0] * 26
        window = [0] * 26
        
        for ch in p:
            tokens[table[ch]] += 1
        
        for i in range(len(p)-1):
            window[table[s[i]]] += 1
            
        ret = []
        index = 0
        for i in range(len(p)-1, len(s)):
            window[table[s[i]]] += 1
            if tokens == window:
                ret.append(index)
            window[table[s[index]]] -= 1
            index += 1
        return ret
```

