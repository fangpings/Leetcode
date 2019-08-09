### 163 Missing Ranges

Given a sorted integer array **nums**, where the range of elements are in the **inclusive range** **[lower, upper]**, return its missing ranges.

**Example:**

```
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
```

### 想法

这道题倒不是特别难，只是边界条件太多了

```python
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if lower == upper:
            if lower in nums:
                return []
            else:
                return [str(lower)]
        if not nums:
            return [str(lower) + '->' + str(upper)]
        ret = []
        last = lower - 1 # last 表示上一个的元素，被初始化为lower - 1是为了和后面的代码一致，即如果lower在nums里面，我们是不会加入lower到ret里面的
        for i in nums:
            if i < lower:
                continue
            elif i > upper: # 当i大于upper的时候，程序就可以结束了（注意i==upper的情况是被认为是普通情况的，即在最后一个else里面处理，如果last==upper即上一个被处理的就是upper了，那这里是不会再去做多余处理了），这时候我们最后判断一下是不是要加入upper
                if upper - last == 1:
                    ret.append(str(upper))
                elif upper - last > 1:
                    ret.append(str(last + 1) + '->' + str(upper))
                break
            else:
                if i - last <= 1: #这里<=是为了防止lower的边界条件
                    last = i
                elif i - last == 2:
                    ret.append(str(i - 1))
                else:
                    ret.append(str(last + 1) + '->' + str(i - 1))
                last = i
        if i < upper: # 如果遍历的最大值也没到upper，那我们还需要最后加入到upper为止的范围
            if upper - last == 1:
                ret.append(str(upper))
            else:
                ret.append(str(last + 1) + '->' + str(upper))
        return ret
```

