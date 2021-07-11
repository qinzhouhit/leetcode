# Write your MySQL query statement below


##
select max(Salary) as SecondHighestSalary 
from Employee where Salary not in (select max(Salary) from Employee)



# version 2
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee)