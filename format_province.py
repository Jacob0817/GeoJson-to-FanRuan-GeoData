# coding=utf-8
import os
import json

def write_json(new_data, country):
    filename="./out/" + country + "-ares.json"
    with open(filename,'r+', encoding="utf-8") as out_file:
        file_data = json.load(out_file)
        file_data["features"].append(new_data)
        out_file.seek(0)
        json.dump(file_data, out_file, indent = 4, ensure_ascii=False)


if __name__ == "__main__":
    path_geojson = "C:\\Users\\Jacob\\Desktop\\gadm36_POL"

    # New json file for fr_world_area
    frjson_head={"type": "FeatureCollection","features": []}

    file_list = os.listdir(path_geojson)
    for geojson_province in file_list:
        if geojson_province[-6:] == "1.json":
            print("Create output file ~ " + geojson_province[-10:-7] + "-ares.json")
            with open("./out/" + geojson_province[-10:-7] + "-ares.json",'w',encoding="utf-8") as out_file:
                json.dump(frjson_head, out_file, indent = 4, ensure_ascii=False)

            print("Read file ~ " + geojson_province)
            with open(path_geojson + "\\" + geojson_province, "r", encoding="utf-8") as f_geojson_province:
                obj_province = json.load(f_geojson_province)
            # print(obj_province["features"][0]["geometry"]["type"])
            for key in range(len(obj_province["features"])):
                # Delete GID_0
                del obj_province["features"][key]["properties"]["GID_0"]
                del obj_province["features"][key]["properties"]["GID_1"]
                del obj_province["features"][key]["properties"]["VARNAME_1"]
                del obj_province["features"][key]["properties"]["NL_NAME_1"]
                del obj_province["features"][key]["properties"]["CC_1"]
                del obj_province["features"][key]["properties"]["HASC_1"]
                # Rename NAME_0 to Area Name
                obj_province["features"][key]["properties"]["name"] = obj_province["features"][key]["properties"].pop("NAME_1")
                write_json(obj_province["features"][0],geojson_province[-10:-7])