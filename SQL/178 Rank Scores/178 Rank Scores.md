### 178 Rank Scores

Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

```
+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
```

For example, given the above `Scores` table, your query should generate the following report (order by highest score):

```
+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
```

### 解析

```SQL
SELECT
  Score,
  (SELECT COUNT(DISTINCT Score) FROM Scores WHERE Score >= s.Score) Rank
FROM Scores s
ORDER BY Score DESC
```

这里有几点需要注意的

1. 别名的AS是可以省略的。而且不仅列可以有别名，表也可以有别名

2. 这个DISTINCT可以放在COUNT里面，虽然没有在书里找到具体的解释，但想必是可以这样弄的

3. 最关键的一点，这里用了作为计算字段的子查询。子查询可以放在WHERE语句里面作为条件集，也可以放在SELECT语句里面作为计算字段来使用。这里对s使用了别名是为了防止子查询的WHERE条件中两个Score列混淆。我们可以把SELECT语句看做对每行查询，对符合条件的行把指定列或者指定列的计算提取出来。这里的子查询相当于对检索出的每个s.Score都进行了一次子查询。如果为了更加清晰一点，我们可以写成这样

4. ```SQl
   SELECT
     s.Score,
     (SELECT COUNT(DISTINCT t.Score) FROM Scores t WHERE t.Score >= s.Score) Rank
   FROM Scores s
   ORDER BY s.Score DESC
   ```

   