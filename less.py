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
import handle_draw as draw


treepath = '/Users/coreygirard/Documents/GitHub/less/chart.yml'
class Chart(object):
    def __init__(self, x=6, y=6):
        self.axes = axes.Axes(x, y, self)

        self._telescope = telescope.Telescope(treepath, self.handle)

        self.stored = {}
        self.load_themes()
        self.themes = themes.ThemesHandler()


        #self.theme_handler = themes.ThemesHandler()
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

    def handle_draw(self, mode, *args, **kwargs):
        args, kwargs = self.themes.apply(args, kwargs)
        # TODO: handle color substitution here
        obj = getattr(draw, mode)(self.axes, *args, **kwargs)


    def handle(self, route):
        plaintext = [e.val for e in route]
        if plaintext in [['plot'],
                         ['scatter'],
                         ['jitter'],
                         ['vbar'],
                         ['hbar']]:
            cmd = route[0]
            assert cmd.type == '()'
            self.handle_draw(cmd.val, *cmd.args, **cmd.kwargs)
        else:
            return self.axes.handle(route)

    def __getitem__(self, k):
        e = self.stored[k]
        return e

    def __getattr__(self, k):
        return getattr(self._telescope, k)

    def get_current_theme(self, style, typ):
        return self.theme[self.current_theme][typ][style]

    def render(self):
        self.axes.render()
