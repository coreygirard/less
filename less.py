import json
import sys
import os

import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import telescope

import handle_axes as axes
import handle_elements as elements
import handle_themes as themes
import handle_colors as colors


treepath = '/Users/coreygirard/Documents/GitHub/less/chart.yml'
class Chart(object):
    def __init__(self, x=6, y=6):
        self.axes = axes.Axes(x, y, self)

        self._telescope = telescope.Telescope(treepath, self.handle)

        self.stored = {}
        self.load_themes()

        self.theme_handler = themes.ThemesHandler()
        self.color_handler = colors.ColorsHandler()

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

    def handle(self, route):
        route = self.theme_handler.apply(route)
        route = self.color_handler.apply(route)
        return self.axes.handle(route)

    def __getitem__(self, k):
        e = self.stored[k]
        return e

    def __getattr__(self, k):
        return getattr(self._telescope, k)

    def get_current_theme(self, style, typ):
        return self.theme[self.current_theme][style][typ]

    def render(self):
        self.axes.render()
