'''
Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
'''

import pandas as pd
data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id':'Int64', 'num':'Int64'})

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    dic = {}
    current = False
    for i in logs['num']:
        if i not in dic.keys():
            dic[i] = 1
            if current is not False:
                if dic[current] < 3:
                    dic[current] = 0
        else:
            if i == current:
                dic[i] += 1
            else:
                if dic[current] < 3:
                    dic[current] = 0
                dic[i] += 1    
        
        current = i
    lista = [k for k, v in dic.items() if v>=3]
    df = pd.DataFrame(lista, columns=['ConsecutiveNums'])
    return df

print(consecutive_numbers(logs))
