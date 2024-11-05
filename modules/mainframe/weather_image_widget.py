import customtkinter as ctk
from .main_frame import main_window
import os
import PIL.Image
from ..read_json import read_json


class WeatherImage(ctk.CTkLabel):
    def __init__(self, child_master: object, **kwrgs):
        ctk.CTkLabel.__init__(
            self, 
            master= child_master, 
            text = '',
            image = self.load_image(),
            fg_color= 'transparent',
            **kwrgs
        )


    def load_image(self):
        data_weather = read_json(name_file= 'config_weather.json')
        weather_icon = data_weather['weather'][0]['icon']
        path_image = os.path.abspath(__file__ + f'/../../../media/images/{weather_icon}.png')
        #
        image = PIL.Image.open(path_image)
        return ctk.CTkImage(light_image= image, size= (170, 160))


weather_image = WeatherImage(child_master= main_window)
weather_image.place(x = 380, y = 170)