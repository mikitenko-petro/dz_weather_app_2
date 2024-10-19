import customtkinter
from ..read_json import read_json
from .frame_manager import city_frame

dict_label = read_json(name_file="config_weather.json")

CITY_NAME= dict_label['name']
CURRENT_TEMP = f'{int(dict_label['main']['temp'])}°'
#
current_position = customtkinter.CTkLabel(
    master= city_frame,
    text = 'Поточна позиція',
    font= ('Arial', 16, 'bold'),
    text_color= '#FFFFFF',
)
current_position.place(x= 14, y= 8)
#
city_name= customtkinter.CTkLabel(
    master= city_frame,
    text= CITY_NAME,
    font= ('Arial', 12, 'bold'),
    text_color= '#FFFFFF',
)
city_name.place(x= 14, y= 33)

current_temp = customtkinter.CTkLabel(
    master= city_frame ,
    text = CURRENT_TEMP,
    font=("Arial", 50 , 'bold'),
    text_color= "#FFFFFF",
)

current_temp.place(x = 165 , y = 12)