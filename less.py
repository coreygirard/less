import matplotlib.pyplot as plt
import numpy as np
import os
from pprint import pprint
import json
import sys
sys.path.append("/Users/coreygirard/Documents/GitHub/telescope")
import telescope

import handle_axes as axes


class Theme(object):
    def __init__(self, data):
        self.data = data

class Chart(object):
    def __init__(self,x=6,y=6):
        self.axes = axes.Axes(x, y, self)

        treepath = '/Users/coreygirard/Documents/GitHub/less/chart.yml'
        self._telescope = telescope.Telescope(treepath,self.handle,k='chart')

        self.stored = {'line':{}}

        self.load_themes()

    def load_themes(self):
        my_path = os.path.dirname(os.path.realpath(__file__))
        self.theme = {}
        for filename in os.listdir(os.path.join(my_path,'themes')):
            if filename.endswith('.json'):
                filepath = os.path.join(my_path,'themes',filename)
                with open(filepath,'r') as f:
                    self.theme[filename[:-5]] = json.load(f)

        if 'default' in self.theme.keys():
            self.current_theme = 'default'
        else:
            assert(len(self.theme.keys()) > 0)
            self.current_theme = sorted(list(self.theme.keys()))[0]


    def handle(self,route,*args,**kwargs):
        temp = []
        for r in route:
            temp += list(r)
        route = (''.join(temp))[1:].split('.')

        head,tail = route[0],route[1:]

        if head in ['spine', 'xlim()', 'ylim()', 'line', 'title()']:
            self.axes.handle(route, *args, **kwargs)
        else:
            print('unknown command:',route,args,kwargs)

    def __getattr__(self,k):
        return getattr(self._telescope,k)

    def get_current_theme(self):
        return self.theme[self.current_theme]

    def plot(self,*args,**kwargs):
        self.axes.plot(*args, **kwargs)

    def scatter(self, *args, **kwargs):
        self.axes.scatter(*args, **kwargs)

    def jitter(self, *args, **kwargs):
        self.axes.jitter(*args, **kwargs)

    def render(self):
        self.axes.render()
