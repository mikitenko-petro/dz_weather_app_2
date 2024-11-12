import customtkinter as ctk
from .main_frame import main_window
import os
import PIL.Image
from ..read_json import read_json


class WeatherImage(ctk.CTkLabel):
    def __init__(self, child_master: object, name_json_weather: str, size: tuple, count: int = 0, **kwrgs):
        self.NAME_JSON_WEATHER = name_json_weather
        self.SIZE = size
        self.COUNT = count
        ctk.CTkLabel.__init__(
            self, 
            master= child_master, 
            text = '',
            fg_color='#5da7b1',
            image = self.load_image(),
            **kwrgs
        )
        
    def load_image(self):
        data_weather = read_json(name_file= self.NAME_JSON_WEATHER)
        if 'weather' in self.NAME_JSON_WEATHER:
            weather_icon = data_weather['weather'][0]['icon']
        elif 'forecast' in self.NAME_JSON_WEATHER:
            weather_icon = data_weather['list'][self.COUNT]['weather'][0]['icon']
        # 
        path_image = os.path.abspath(__file__ + f'/../../../media/images/{weather_icon}.png')
        #
        image = PIL.Image.open(path_image)
        return ctk.CTkImage(light_image= image, size= self.SIZE)


weather_image = WeatherImage(child_master= main_window, name_json_weather= 'config_weather.json', size= (170, 160))
weather_image.place(x = 380, y = 170)