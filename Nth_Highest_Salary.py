'''
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.
'''

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    nome_coluna = f'getNthHighestSalary({N})'
    employee.sort_values(by=["salary", "id"], ascending=[False,True], inplace=True)
    employee.drop_duplicates(subset=["salary"], keep="first", inplace=True)

    if N > employee.shape[0] or N<=0:
        return pd.DataFrame({nome_coluna: None}, index=[0])
    saida = pd.DataFrame({nome_coluna: employee[["salary"]].iloc[N-1]})
    return saida

employee = pd.DataFrame({"id": [1, 2], "salary": [1000, 2000]})

print(nth_highest_salary(employee, 2))

