#Create unit tests

import unittest
from weatherclass import WeatherApi

class TestWeather(unittest.TestCase):

#unit test to see if get_weatherdata() function populated my list "average temp"
    def test_get_weatherdata_avg_temp(self):
        test_weather = WeatherApi(latitude=30.2672,longitude =-97.7431,year=2024, month=4, day=1)
        test_weather.get_weatherdata()
        self.assertNotEqual(len(test_weather.average_temp), 0)
#unit test to see if get_weatherdata() function populated my list "max_wind_speed"
    def test_get_weatherdata_max_wind_speed(self):
        test_weather = WeatherApi(latitude=30.2672,longitude =-97.7431,year=2024, month=4, day=1)
        test_weather.get_weatherdata()
        self.assertNotEqual(len(test_weather.max_wind_speed), 0)
#unit test to see if get_weatherdata() function populated my list "sum_precipitation"
    def test_get_weatherdata_sum_precipitation(self):
        test_weather = WeatherApi(latitude=30.2672,longitude =-97.7431,year=2024, month=4, day=1)
        test_weather.get_weatherdata()
        self.assertNotEqual(len(test_weather.sum_precipitation), 0)

if __name__ == '__main__':
    unittest.main()

