### 177 Nth Highest Salary

Write a SQL query to get the *n*th highest salary from the `Employee` table.

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

For example, given the above Employee table, the *n*th highest salary where *n* = 2 is `200`. If there is no *n*th highest salary, then the query should return `null`.

```
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```

### 解析

这道题新的知识点主要是SQL的函数？

函数模板如下

```SQL
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M=N-1;
  RETURN (
    SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET M
  );
END
```

1. 创建函数： create Function 函数名称 (输入参数变量，类型) RETURNS 类型 begin ... return 返回值 end (中间是具体实现)
2.  变量定义关键字：declare 变量名+类型。
3. 流程控制: if(condition)then ...elseif(condition)  then ... else...  end if;
4. 变量赋值: select ..into 变量名 或者是 set 变量名=value

