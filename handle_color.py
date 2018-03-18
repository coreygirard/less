from pprint import pprint
import json
import matplotlib.pyplot as plt
import re


def load_colors():
    with open('colors.json', 'r') as f:
        data = json.load(f)

    temp = {}
    for k, v in data.items():
        # catches 'black' and 'white', which have only one flavor
        if type(v) == str:
            temp[k] = v
            continue

        # in Google's MDL, 'red' is equivalent to 'red-500'
        temp[k] = v['500']
        for n, hx in v.items():
            temp['{0}-{1}'.format(k, n)] = hx

    return temp

data = load_colors()
pprint(data)

hex_three = '#[0-9a-fA-F]{3}'
hex_six = '#[0-9a-fA-F]{6}'
def parse(color):
    # matches 'red-700', etc
    if color in data.keys():
        return data[color]

    # matches '#f4b', etc
    if re.fullmatch(hex_three, color):
        expanded = ''.join([color[i] for i in [0, 1, 1, 2, 2, 3, 3]])
        return expanded

    # matches '#45d2bc', etc
    if re.fullmatch(hex_six, color):
        return color

#print(parse('#abc'))
#print(parse('#01f5ab'))
#print(parse('light-blue-700'))
