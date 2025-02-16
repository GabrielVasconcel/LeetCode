'''
Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

The result format is in the following example.

Example 1:

Input: 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output: 
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
'''

import pandas as pd

data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-03-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    count = 0
    for id in activity['player_id'].unique():
        slice = activity[activity['player_id'] == id]
        event_dates = sorted(slice['event_date'].unique())

        if len(event_dates) >= 2 and (event_dates[1] - event_dates[0]).days == 1:
            count += 1
            
    
    fraction = count / len(activity['player_id'].unique())  
    return pd.DataFrame([fraction], columns=['fraction']).round(2)

print(gameplay_analysis(activity))