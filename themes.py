
default = {
    "background": {
        "plot": {
            "color": "#BBBBBB"
        },
        "scatter": {
            "s": 3,
            "color": "grey"
        },
        "spines": {
            "color": "#999999"
        },
        "ticks": {
            "color": "#999999"
        }
    },
    "highlight": {
        "scatter": {
            "c": "r",
            "s": 9
        }
    }
}


import json
from pprint import pprint

with open('default_theme.json','w') as f:
    json.dump(default,f,indent=4,sort_keys=True)

'''
for line in json.dumps(default,
                       indent=4,
                       sort_keys=True).split('\n'):
    print(line)
'''
