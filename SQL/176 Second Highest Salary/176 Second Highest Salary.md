### 176 Second Highest Salary

Write a SQL query to get the second highest salary from the `Employee` table.

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

For example, given the above Employee table, the query should return `200` as the second highest salary. If there is no second highest salary, then the query should return `null`.

```
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

### 解析

```sql
SELECT max(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary NOT IN (SELECT max(Salary) FROM Employee); 
```

不太熟悉的知识点有下面三个

1. 别名AS，这个是对选中的列生成一个新的名字。事实上计算列（即使用函数生成的列）是没有名字的，我们需要使用AS来起一个名字
2. 计算函数和计算字段。这里我们使用了`max()`函数来对选中的Salary列进行计算来生成新的列
3. 子查询。WHERE中NOT IN括号中的就是子查询，相当于我们外层的查询是在子查询已经查到的表作为限制条件进行查询的。

```SQL
SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
```

这种写法是选择第k位的一种常用写法，但这种写法为什么不行呢？因为当表中只有1个元素的时候，它是不会返回任何值的，但是我们要求返回NULL。**事实上如果查询语句没有查询到任何东西，它默认是什么也不返回的。**

我们的写法为什么可以呢，**那是因为使用`max()`函数之类的，当没有传入值的时候会返回NULL**。