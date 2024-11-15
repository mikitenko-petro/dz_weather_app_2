import customtkinter as ctk
from .horizontal_scroll import h_scroll
from .weather_image_widget import WeatherImage
from .hourly_forecast_time import HourlyForecastTime

class HourlyForecast(ctk.CTkFrame):
    def __init__(self, child_master: object, count: int = 0,  **kwargs):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            fg_color= '#5da7b1',
            **kwargs
        )
        #
        self.COUNT = count
        #
        self.grid(row= 0, column = self.COUNT, padx= 20)
        #
        self.TIME = HourlyForecastTime(child_master= self, count= self.COUNT)
        self.TIME.pack(anchor= 'center')
        #
        self.IMAGE = WeatherImage(
            child_master= self,
            name_json_weather= "config_forecast.json",
            size= (70, 70),
            count= self.COUNT
        )
        self.IMAGE.pack(anchor= 'center', pady= 20)

for el in range(3):
    hourly_forecast = HourlyForecast(child_master= h_scroll, count= el)