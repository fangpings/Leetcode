### 187 Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

**Example:**

```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```

### 想法

把每个长度为10的substring都放到hashtable里面，统计词数超过两次的key。

注意用dict其实很慢，更快的方法是用set(虽然理论上都是O(1)，但是set明显更快)

用两个set，一个记录所有的substring，一个记录在前一个里面出现过，又出现的substring