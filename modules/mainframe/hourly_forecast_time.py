import os
import customtkinter as ctk
from ..read_json import read_json


class HourlyForecastTime(ctk.CTkLabel):
    def __init__(self, child_master: object, count: int = 0, **kwrgs):

        ctk.CTkLabel.__init__(
            self, 
            master= child_master, 
            text = self.load_text(count = count),
            font= ("Arial", 32, "bold"),
            fg_color='#5da7b1',
            **kwrgs
        )
        
    def load_text(self, count):
        data_weather = read_json(name_file= "config_forecast.json")
        time = data_weather['list'][count]["dt_txt"]
        trimmed_time = time[11 : 16]
        return trimmed_time
        
