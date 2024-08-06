import requests
import json

#Create class with the required instance variables
class WeatherApi:
    def __init__(self,latitude, longitude, year, month, day):
        self.latitude = latitude
        self.longitude = longitude
        self.year = year
        self.month = month
        self.day = day
        self.average_temp = []
        self.min_temp = []
        self.max_temp = []
        self.avg_wind_speed = []
        self.min_wind_speed = []
        self.max_wind_speed = []
        self.sum_precipitation = []
        self.min_precipitation = []
        self.max_precipitation = []

    #Method to change the base_url to select the start and end dates
    def get_weatherdata(self):
        base_url = 'https://archive-api.open-meteo.com/v1/archive'

#Define parameters
        params = {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'start_date': f'{self.year}-{self.month:02d}-{self.day:02d}',
            'end_date': f'{self.year}-{self.month:02d}-{self.day:02d}',
            'daily':'temperature_2m_mean,precipitation_sum,wind_speed_10m_max',
            'temperature_unit': 'fahrenheit',
            'wind_speed_unit': 'mph',
            'precipitation_unit': 'inch',
            'timezone': 'America/Chicago',
        }

        #Forloop to walk backwards from specified year (ex:2024) to the year that we want to end at (2020)
        for i in range(self.year - 4, self.year + 1):
            start_date = f'{i}-{self.month:02d}-{self.day:02d}'
            end_date = f'{i}-{self.month:02d}-{self.day:02d}'
            params['start_date'] = start_date
            params['end_date'] = end_date
            url = f"{base_url}?latitude={self.latitude}&longitude={self.longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago"
            response = requests.get(url, params=params)
        

            #IF statement to ensure there are no errors by checking for status code == 200
            # IF there are no errors, we will grab the values of interest(mean temp, max wind speed, and sum of precipitation)
            #Nested if-statements help identify any errors
            if response.status_code == 200:
                try:
                    data = response.json()
                    for j in data:
                        if 'daily' in j:
                            daily_data = j['daily']
                            if (
                                'temperature_2m_mean' in daily_data
                                and 'wind_speed_10m_max' in daily_data
                                and 'precipitation_sum' in daily_data):

                                temp_mean = daily_data['temperature_2m_mean'][0]
                                self.average_temp.append(temp_mean)
                                wind_speed_max = daily_data['wind_speed_10m_max'][0]
                                self.max_wind_speed.append(wind_speed_max)
                                percip_sum = daily_data['precipitation_sum'][0]
                                self.sum_precipitation.append(percip_sum)

                            else:
                                print ('Cannot find parameters in Daily Data')
                        else:
                            print ('Cannot fine Daily Data')
                except json.decoder.JSONDecodeError:
                    print('JSONDecodeError')
            else:
                print('Error!', {response.status_code})

    #Separate methods for each of the daily weather variables
    def get_avg_temp(self):
        avg_temp_list_comp = [int(x) for x in self.average_temp]
        final_avg_temp = sum(avg_temp_list_comp) / len(avg_temp_list_comp)
        print(f'This is the Average Temp in Austin for the last 5 Yrs: {final_avg_temp} Fahrenheit')

    def get_max_wind_speed(self):
        max_wind_speed_list_comp = [int(x) for x in self.max_wind_speed]
        final_max_wind_speed = max(max_wind_speed_list_comp)
        print(f'This is the Max Wind Speed in Austin for the last 5 Yrs: {final_max_wind_speed} mph')

    def get_sum_precipitation(self):
        sum_precipitation_list_comp = [int(x) for x in self.sum_precipitation]
        final_sum_precipitation = sum(sum_precipitation_list_comp)
        print(f'This is the Sum of Precipitation in Austin for the last 5 Yrs: {final_sum_precipitation} inches')
