# Write your MySQL query statement below
SELECT 
    d.Name AS 'Department',
    e.Name AS 'Employee',
    e.Salary AS 'Salary'
FROM
    (SELECT DepartmentId, MAX(Salary) AS 'MaxSalary'
    FROM Employee
    GROUP BY DepartmentId) as sq
JOIN Employee AS e
ON sq.MaxSalary = e.Salary
AND sq.DepartmentId = e.DepartmentId
JOIN Department AS d
ON d.Id = e.DepartmentId