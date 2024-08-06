from weatherclass import WeatherApi
from weathertableclass import WeatherTable, session, engine
from sqlalchemy.orm import sessionmaker
import sqlite3

#Initialize WeatherApi
austintx = WeatherApi(latitude=30.2672,longitude =-97.7431,year=2024, month=4, day=1)
austintx.get_weatherdata()

#Calculate weather statistics 
austintx.get_avg_temp()
austintx.get_max_wind_speed()
austintx.get_sum_precipitation()

#Populate WeatherTable using a for loop and session commands
current_yr = austintx.year
last_five_yr =range(current_yr,current_yr-5,-1)
month = austintx.month
day = austintx.day

for year in last_five_yr:
    index = current_yr - year
    weather_data = WeatherTable(
        latitude=austintx.latitude,
        longitude=austintx.longitude,
        year=year,
        month=month,
        day=day,
        five_yr_avg_temp=austintx.average_temp[index],
        five_yr_max_wind_speed=austintx.max_wind_speed[index],
        five_yr_sum_precipitation=austintx.sum_precipitation[index],
    )
    session.add(weather_data)

    
    
#Commit all changes
session.commit()

#Query the table
session = sessionmaker(bind=engine)
conn = sqlite3.connect('weathertable.db')
c = conn.cursor()
cursor = c.execute('SELECT * FROM Weather_Information')
results = cursor.fetchall()
for row in results:
    print(row)

conn.close()
