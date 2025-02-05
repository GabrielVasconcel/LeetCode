import pandas as pd
'''
The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Trips table:
+----+-----------+-----------+---------+---------------------+------------+
| id | client_id | driver_id | city_id | status              | request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+
Users table:
+----------+--------+--------+
| users_id | banned | role   |
+----------+--------+--------+
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |
+----------+--------+--------+
Output: 
+------------+-------------------+
| Day        | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |
+------------+-------------------+
'''

data = [['1', '1', '10', '1', 'completed', '2013-10-01'], ['2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01'], ['3', '3', '12', '6', 'completed', '2013-10-01'], ['4', '4', '13', '6', 'cancelled_by_client', '2013-10-01'], ['5', '1', '10', '1', 'completed', '2013-10-02'], ['6', '2', '11', '6', 'completed', '2013-10-02'], ['7', '3', '12', '6', 'completed', '2013-10-02'], ['8', '2', '12', '12', 'completed', '2013-10-03'], ['9', '3', '10', '12', 'completed', '2013-10-03'], ['10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03']]
trips = pd.DataFrame(data, columns=['id', 'client_id', 'driver_id', 'city_id', 'status', 'request_at']).astype({'id':'Int64', 'client_id':'Int64', 'driver_id':'Int64', 'city_id':'Int64', 'status':'object', 'request_at':'object'})

data = [['1', 'No', 'client'], ['2', 'Yes', 'client'], ['3', 'No', 'client'], ['4', 'No', 'client'], ['10', 'No', 'driver'], ['11', 'No', 'driver'], ['12', 'No', 'driver'], ['13', 'No', 'driver']]
users = pd.DataFrame(data, columns=['users_id', 'banned', 'role']).astype({'users_id':'Int64', 'banned':'object', 'role':'object'})

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # filtrar por viagens de usuários(clientes ou motoristas) não banidos
    unbanned = users[users['banned'] == 'No']['users_id']
    trips = trips[trips['client_id'].isin(unbanned) & trips['driver_id'].isin(unbanned)]
    # recorte de tempo
    trips['request_at'] = pd.to_datetime(trips['request_at'], format='%Y-%m-%d')
    trips = trips[(trips['request_at'] >= '2013-10-01') & (trips['request_at'] <= '2013-10-03')]

    all_dates = pd.DataFrame({'request_at': trips['request_at'].unique()})
    # agrupar por data e contar o total de viagens
    total_trips = trips.groupby('request_at').size().reset_index(name='total_trips')
    total_cancelled = trips[trips['status'].str.contains('cancelled')].groupby('request_at').size().reset_index(name='total_cancelled')
    all_dates = all_dates.merge(total_cancelled, on='request_at', how='left').fillna(0)
    total_trips = total_trips.merge(all_dates, on='request_at', how='left').fillna(0)
    total_trips['Cancellation Rate'] = (total_trips['total_cancelled'] / total_trips['total_trips']).round(2)
    total_trips = total_trips.drop(columns=['total_cancelled', 'total_trips'])
    total_trips = total_trips.rename(columns={'request_at':'Day'})

    return total_trips

print(trips, '\n',trips_and_users(trips, users))