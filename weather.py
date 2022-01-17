from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from datetime import datetime
import os




class Weather:
    def __init__(self):
        api_key = '5aeb479d2c3bfd72033c1254fd6d352d'
   
        owm = OWM(api_key)
        self.mgr = owm.weather_manager()

        observation = self.mgr.weather_at_place('Los Angeles')
        self.weather = observation.weather

    # forecast = mgr.forecast_at_place('Milan,IT', 'daily')
    def temp(self):
        return self.weather.temperature('fahrenheit').get('temp')

    def description(self): 
        return self.weather.detailed_status
    def sunset(self):
        date_time = datetime.fromtimestamp(self.weather.sunset_time())
        d = date_time.strftime("%I:%M %p")
        return d
    def sunrise(self):
        date_time = datetime.fromtimestamp(self.weather.sunrise_time())
        d = date_time.strftime("%I:%M %p")
        return d
    def forecast(self):
        forecast = self.mgr.forecast_at_place('Los Angeles, CA', 'daily')
        return forecast



