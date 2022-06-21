import os
import re
import json

def write_json(new_data, filename="./out/world-ares.json"):
    with open(filename,'r+') as out_file:
        file_data = json.load(out_file)
        file_data["features"].append(new_data)
        out_file.seek(0)
        json.dump(file_data, out_file, indent = 4)

# write_json(obj_country["features"][0])

if __name__ == "__main__":
    path_geojson = "C:\\Users\\Jacob\\Desktop\\gadm36_POL"

    # New json file for fr_world_area
    frjson_head={"type": "FeatureCollection","features": []}
    with open("./out/world-ares.json",'w') as out_file:
        json.dump(frjson_head, out_file, indent = 4)

    file_list = os.listdir(path_geojson)
    for geojson_country_name in file_list:
        if geojson_country_name[-6:] == "0.json":
            print("Read file ~ " + geojson_country_name)
            with open(path_geojson + "\\" + geojson_country_name,"r") as f_geojson_country:
                obj_country = json.load(f_geojson_country)
            # Set type value to Polygon
            obj_country["features"][0]["geometry"]["type"]= "Polygon"
            # print(obj_country["features"][0]["geometry"]["type"])
            # Delete GID_0
            del obj_country["features"][0]["properties"]["GID_0"]
            # Rename NAME_0 to Area Name
            obj_country["features"][0]["properties"]["Area Name"] = obj_country["features"][0]["properties"].pop("NAME_0")
            # print(obj_country["features"][0]["properties"]["Area Name"])
            write_json(obj_country["features"][0])