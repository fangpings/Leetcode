### 76 Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

**Example:**

```
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

**Note:**

- If there is no such window in S that covers all characters in T, return the empty string `""`.
- If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

#### 想法

这题用到的方法叫**Sliding Window Approach**，即维护一个动态的Sliding Window(指window的左右两端一直在滑动)

我们先从左往右找到第一个能包括目标字符串T里面所有字符的S中的Window，左端和右端分别用L和R指代。在找到了最初的Window之后，我们开始继续向右调整Window的大小。我们先从左缩减Window，记录缩减掉的目标字符，再从右扩张Window，直到被缩减掉的字符重新被包括在Window中，然后我们记录此时Window的长度并与全局长度进行对比。

自己实现的代码很垃圾，贴一个比较好的代码

```python
from collections import defaultdict
class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        mem = defaultdict(int)  # 利用dict记录t中字符还需要在s中遇到的次数 
        for c in t:
            mem[c] += 1  
        t_len = len(t)  # 利用t_len记录已经遇到的t中的字符
        
        minL, minR = 0, float('inf')
        
        l = 0
        
        for i, c in enumerate(s):
            if mem[c] > 0:  # mem[c] > 0 代表c字符仍然有缺失
                t_len -= 1
            
            mem[c] -= 1
            
            if t_len == 0:  # 此时一个window已经成立了，该window包含了t中的所有字符
                while mem[s[l]] < 0:  # 开始更新，这一步是关键，mem[s[l]] < 0代表这个字符实际上是多余的，所以可以直接去掉。这一步我们不管s[l]在不在t里面，只要他< 0, 那肯定是多余的直接删掉就行了
                    mem[s[l]] += 1
                    l += 1
                
                if i - l < minR - minL:
                    minR, minL = i, l
             
                mem[s[l]] += 1 # 到第一个=0的地方，注意这里肯定不会出现不在t中的字符，所以第一个=0的地方就是我们要删掉的非多余第一个目标字符(之所以说是非多余是因为目标字符也有可能重复的，表现为mem[c] < 0)
                t_len += 1
                l += 1  # 然后我们继续向右拓展window
        return '' if minR == float('inf') else s[minL:minR+1]
```

