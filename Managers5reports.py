import pandas as pd

'''
Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+
'''

data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(employee, how='left',left_on='managerId', right_on='id', suffixes=('', '_manager')).drop(columns='managerId_manager')
    managers = employee.groupby('id_manager').size().to_frame('reports').reset_index()
    managers5 = managers[managers['reports']>=5]
    employee = employee[employee['id'].isin(managers5['id_manager'])]

    return employee['name'].to_frame('name')

print(find_managers(employee))