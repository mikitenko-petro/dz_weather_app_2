import os
import json

def create_json(name_file: str, name_dict: dict):
    path_file = os.path.abspath(__file__ + f"../../../static/{name_file}")
    with open(file= path_file, mode= "w") as file_json:
        json.dump(
            obj= name_dict, #
            fp= file_json, #
            ensure_ascii= False, #
            indent= 4
        )
 