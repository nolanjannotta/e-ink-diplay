from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from datetime import datetime
import os




class Weather:
    def __init__(self):
        api_key = os.environ.get('WEATHER_API') 
   
        owm = OWM(api_key)
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place('Los Angeles')
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
        # forecast = mgr.forecast_at_place('Milan,IT', 'daily')
        pass





