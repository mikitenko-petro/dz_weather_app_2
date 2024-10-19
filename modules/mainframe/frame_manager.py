import customtkinter
from .main_frame import main_window, HEIGHT, WIDTH

#
window_frame = customtkinter.CTkFrame(
    master= main_window, 
    width= WIDTH, 
    height= HEIGHT,
    fg_color= '#5DA7B1',
    bg_color= '#096C82',
    # border_width= 5,
    # corner_radius= 20
    
)
#
window_frame.pack(fill= "both", expand= True)
#
scrollable_frame = customtkinter.CTkScrollableFrame(
    master= window_frame, 
    width= 275, 
    height= HEIGHT,
    fg_color= '#096C82',
    # border_width= 5,
    # bg_color= '#096C82',

)
# scrollable_frame.pack(side= "left", fill= "both", expand= True)
scrollable_frame.grid(row=0, column=0, sticky="nsew")
#
city_frame = customtkinter.CTkFrame(
    master= scrollable_frame,
    width= 235,
    height= 100,
    fg_color= "#4599A4",
    border_width= 2,
    border_color= "#FFFFFF",
    corner_radius= 20,
)
city_frame.pack(anchor= "center", expand= True)