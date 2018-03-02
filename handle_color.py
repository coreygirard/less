from pprint import pprint
import json
import matplotlib.pyplot as plt


with open('colors.json', 'r') as f:
    data = json.load(f)

def convert(h):
    return int(h[1:3],16),int(h[3:5],16),int(h[5:7],16)

with open('colors.json','r') as f:
    data = json.load(f)
