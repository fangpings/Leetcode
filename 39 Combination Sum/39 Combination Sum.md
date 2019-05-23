### 39 Combination Sum

Given a **set** of candidate numbers (`candidates`) **(without duplicates)** and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

The **same** repeated number may be chosen from `candidates` unlimited number of times.

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

### 40 Combination Sum II

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

**Example 2:**

```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

#### 想法

这两题差不多。有两点，一点是如何递归的找（我觉得这个应该是DP的一种？），第二点是如何避免重复。递归的找的话，我们遍历整个candidates，对每个candidate，我们从target中减去他作为新的target，然后把他加入候选名单，如果target减candidate=0，那么我们直接把传过来的候选名单加入return值。对于防止重复，我们先对整个列表进行排序，然后每次递归的时候，对于39每个数能被使用无限次而列表内没有重复元素，我们只向下一级传当前位置以及之后的candidates。对于40每个数只能使用一次但是会有重复元素，我们每次向下一级传当前位置之后的所有元素，并在每一个位置递归结束之后，**跳过所有的相同元素**

