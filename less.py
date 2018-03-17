import json
import sys
import os

import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
sys.path.append("/Users/coreygirard/Documents/GitHub/telescope")
import telescope

import handle_axes as axes
import handle_elements as elements


class Theme(object):
    def __init__(self, data):
        self.data = data

treepath = '/Users/coreygirard/Documents/GitHub/less/chart.yml'
class Chart(object):
    def __init__(self, x=6, y=6):
        self.axes = axes.Axes(x, y, self)

        self._telescope = telescope.Telescope(treepath, self.handle, k='chart')

        self.stored = {}

        self.load_themes()

    def load_themes(self):
        my_path = os.path.dirname(os.path.realpath(__file__))
        self.theme = {}
        for filename in os.listdir(os.path.join(my_path, 'themes')):
            if filename.endswith('.json'):
                filepath = os.path.join(my_path, 'themes', filename)
                with open(filepath, 'r') as f:
                    self.theme[filename[:-5]] = json.load(f)

        if 'default' in self.theme.keys():
            self.current_theme = 'default'
        else:
            assert len(self.theme.keys()) > 0
            self.current_theme = sorted(list(self.theme.keys()))[0]


    def handle(self, route, *args, **kwargs):
        temp = []
        for r in route:
            temp += list(r)
        route = (''.join(temp))[1:].split('.')

        self.axes.handle(route, *args, **kwargs)

    def __getitem__(self, k):
        e = self.stored[k]
        return e

    def __getattr__(self, k):
        return getattr(self._telescope, k)

    def get_current_theme(self, style, typ):
        return self.theme[self.current_theme][style][typ]

    '''
    def plot(self, *args, **kwargs):
        self.axes.plot(*args, **kwargs)

    def scatter(self, *args, **kwargs):
        self.axes.scatter(*args, **kwargs)

    def jitter(self, *args, **kwargs):
        self.axes.jitter(*args, **kwargs)

    def vbar(self, *args, **kwargs):
        self.axes.vbar(*args, **kwargs)

    def hbar(self, *args, **kwargs):
        self.axes.hbar(*args, **kwargs)
    '''

    def render(self):
        self.axes.render()
