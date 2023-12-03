import json
import csv
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
) 

def convert_rgb_to_names(rgb_tuple):
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f'{names[index]}'

def createCsv():
    data_file = open('data_file.csv', 'w')
    csv_writer = csv.writer(data_file)
    
    count = 0
    for emp in data:
        if count == 0: 
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(emp.values()) 
    data_file.close()

# Opening JSON file
f = open('data.json')
data = json.load(f)
for i in data:
    i['color'] = convert_rgb_to_names((i['r'], i['g'], i['b']))
    del i['r']
    del i['g']
    del i['b']
f.close()
createCsv()
