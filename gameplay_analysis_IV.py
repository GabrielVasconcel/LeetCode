import pandas as pd

data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-03-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    count = 0
    for id in activity['player_id'].unique():
        slice = activity[activity['player_id'] == id]
        event_dates = sorted(slice['event_date'].unique())
    
        if any((event_dates[i+1] - event_dates[i]).days == 1 for i in range(len(event_dates)-1)):
            count += 1
            
    
    fraction = count / len(activity['player_id'].unique())  
    return pd.DataFrame([fraction], columns=['fraction']).round(2)

print(gameplay_analysis(activity))