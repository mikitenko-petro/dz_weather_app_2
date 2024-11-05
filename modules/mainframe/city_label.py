import customtkinter
from ..read_json import read_json
from .frame_manager import scrollable_frame

dict_label = read_json(name_file="config_weather.json")

CITY_NAME= dict_label['name']
CURRENT_TEMP = f"{int(dict_label['main']['temp'])}°"
MAX_TEMP = f"макс.: {int(dict_label['main']['temp_max'])}°"
MIN_TEMP = f"мін.: {int(dict_label['main']['temp_min'])}°"
WEATHER_DESCRIPTION = dict_label['weather'][0]['description'].capitalize()
#
class CityFrame(customtkinter.CTkFrame):
    def __init__(self, child_master: object, **kwargs):
        customtkinter.CTkFrame.__init__(
            self, 
            master= child_master, 
            width= 250, 
            height= 100, 
            fg_color= "#4599A4",
            border_width= 2,
            border_color= "#FFFFFF",
            corner_radius= 20,
            **kwargs
        )
        self.pack(anchor= "center", expand= True, pady= 20)  
        # 
        self.CURRENT_POSITION = customtkinter.CTkLabel(
            master= self,
            text = 'Поточна позиція',
            font= ('Roboto Slab', 16, 'bold'),
            text_color= '#FFFFFF',
        )
        self.CURRENT_POSITION.place(x = 14, y = 8)
        #
        self.CURRENT_TEMP = customtkinter.CTkLabel(
            master= self,
            text = CURRENT_TEMP,
            font=("Roboto Slab", 50, 'bold'),
            text_color= "#FFFFFF",
        )
        self.CURRENT_TEMP.place(x = 160, y = 6)
        #
        self.CITY_NAME = customtkinter.CTkLabel(
            master = self,
            text = CITY_NAME,
            font = ("Roboto Slab", 12, "bold"),
            text_color = "#FFFFFF" 
        )
        self.CITY_NAME.place(x = 14, y = 33)
        #
        self.MAX_TEMP = customtkinter.CTkLabel(
            master = self,
            text = MAX_TEMP,
            font = ("Roboto Slab", 12, "bold"),
            text_color = "#f7f4f3" 
        )
        self.MAX_TEMP.place(x = 110, y = 65)
        #
        self.MIN_TEMP = customtkinter.CTkLabel(
            master = self,
            text = MIN_TEMP,
            font = ("Roboto Slab", 12, "bold"),
            text_color = "#f7f4f3" 
        )
        self.MIN_TEMP.place(x = 175, y = 65)
        #
        self.WEATHER_DESCRIPTION = customtkinter.CTkLabel(
            master = self,
            text = WEATHER_DESCRIPTION,
            font = ("Roboto Slab", 12, "bold"),
            text_color = "#f7f4f3" 
        )
        self.WEATHER_DESCRIPTION.place(x = 14, y = 65)


for i in range(10):
    city_frame = CityFrame(child_master= scrollable_frame)