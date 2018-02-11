import matplotlib.pyplot as plt
import numpy as np
import os
from pprint import pprint
import json
import sys
sys.path.append("/Users/coreygirard/Documents/GitHub/telescope")
import telescope


class Theme(object):
    def __init__(self, data):
        self.data = data

class Chart(object):
    def __init__(self,x=6,y=6):
        self.fig = plt.figure(figsize=(x,y))

        self.axes = {}
        self.axes['left'] = self.fig.subplots()
        self.axes['right'] = self.axes['left'].twinx()
        self.axes['top'] = self.axes['left'].twiny()
        self.axes['bottom'] = self.axes['top'].twiny()

        self.axes['left'].yaxis.set_ticks_position('left')
        self.axes['right'].yaxis.set_ticks_position('right')
        self.axes['top'].xaxis.set_ticks_position('top')
        self.axes['bottom'].xaxis.set_ticks_position('bottom')

        self.axes['left'].yaxis.set_label_position('left')
        self.axes['right'].yaxis.set_label_position('right')
        self.axes['top'].xaxis.set_label_position('top')
        self.axes['bottom'].xaxis.set_label_position('bottom')

        self.spines_lookup = {'left':self.axes['left'].spines['left'],
                              'right':self.axes['right'].spines['right'],
                              'top':self.axes['top'].spines['top'],
                              'bottom':self.axes['bottom'].spines['bottom']}
        self.ticks_lookup = {'left':self.axes['left'].set_yticks,
                             'right':self.axes['right'].set_yticks,
                             'top':self.axes['top'].set_xticks,
                             'bottom':self.axes['bottom'].set_xticks}
        self.labels_lookup = {'left':self.axes['left'].set_yticklabels,
                              'right':self.axes['right'].set_yticklabels,
                              'top':self.axes['top'].set_xticklabels,
                              'bottom':self.axes['bottom'].set_xticklabels}

        treepath = '/Users/coreygirard/Documents/GitHub/less/chart.yml'
        self._telescope = telescope.Telescope(treepath,self.handle,k='chart')

        self.stored = {'line':{}}

        self.load_themes()
        self.kill_all()

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

        if head == 'spine':
            self.handle_spine(tail,args,kwargs)
        elif head == 'xlim':
            self.handle_xlim(tail,args,kwargs)
        elif head == 'ylim':
            self.handle_ylim(tail,args,kwargs)
        elif head == 'line':
            self.handle_line(tail,args,kwargs)
        elif head == 'title()':
            self.axes['left'].set_title(args[0])
        else:
            print('unknown command:',route,args,kwargs)

    def handle_spine(self,route,args,kwargs):
        #assert(len(route) == 2)
        assert(route[0] in self.spines_lookup.keys())

        spine,cmd = route[0],route[1:]

        if cmd == ['visible()']:
            assert(args[0] in [True,False])
            self.spines_lookup[spine].set_visible(args[0])
        elif cmd == ['bounds']:
            assert(len(args[0]) == 2)
            self.spines_lookup[spine].set_bounds(*args[0])
        elif cmd == ['ticks','major()']:
            self.handle_spine_ticks(spine,cmd,args,kwargs)
        elif cmd == ['ticks','minor()']:
            self.handle_spine_ticks_minor(spine,cmd,args,kwargs)
        elif cmd == ['label()']:
            self.set_axis_label(spine,args,kwargs)

    def handle_spine_ticks(self,spine,cmd,args,kwargs):
        self.ticks_lookup[spine](args[0])
        self.axes[spine].tick_params(**{spine:'on'})

        labels = kwargs.get('labels',False)
        if labels == False:
            self.labels_lookup[spine](args[0])
        else:
            assert(type(labels) == list)
            self.labels_lookup[spine](labels)

        self.axes[spine].tick_params(**{'label'+spine:'on'})

        leave_bounds = kwargs.get('leavebounds',False)
        if leave_bounds != True:
            self.spines_lookup[spine].set_bounds(min(args[0]),max(args[0]))

    def handle_spine_ticks_minor(self,spine,cmd,args,kwargs):
        self.ticks_lookup[spine](args[0],minor=True)

    def handle_ylim(self,route,args,kwargs):
        self.axes['left'].set_ylim(*args)
        self.sync_scales()

    def handle_xlim(self,route,args,kwargs):
        self.axes['left'].set_xlim(*args)
        self.sync_scales()

    def handle_line(self,route,args,kwargs):
        if route == ['label()']:
            self.handle_line_label(args,kwargs)

    def handle_line_label(self,args,kwargs):
        for line in self.stored['line'][kwargs['line']]:
            x,y = line.get_xydata()[-1]
            color = kwargs.get('color',line.get_color())
            self.axes['left'].text(x+0.1,y,
                                   kwargs['label'],
                                   verticalalignment='center',
                                   color=color)

    def set_axis_label(self,spine,args,kwargs):
        if spine == 'left':
            self.axes['left'].set_ylabel(args[0])
        elif spine == 'bottom':
            self.axes['bottom'].set_xlabel(args[0])

    def __getattr__(self,k):
        return getattr(self._telescope,k)

    def kill_all(self):
        for axes in [self.axes['left'],
                     self.axes['right'],
                     self.axes['top'],
                     self.axes['bottom']]:

            params = {}
            for k in ['left','right','top','bottom']:
                params[k] = 'off'
                params['label'+k] = 'off'
            axes.tick_params(axis='both',**params)
            for s in ['top','bottom','left','right']:
                axes.spines[s].set_visible(False)

    def sync_scales(self):
        self.axes['right'].set_ylim(*self.axes['left'].get_ylim())
        self.axes['top'].set_xlim(*self.axes['left'].get_xlim())
        self.axes['bottom'].set_xlim(*self.axes['left'].get_xlim())

    def plot(self,*args,**kwargs):
        assert(len(args) == 0)

        if 'style' not in kwargs: kwargs['style'] = 'background'

        d = self.theme[self.current_theme][kwargs['style']]['plot']

        for k in ['color','linestyle']:
            if k in kwargs:
                d[k] = kwargs[k]

        name = kwargs.pop('name',None)
        line = self.axes['left'].plot(kwargs['x'],
                                      kwargs['y'],
                                      **d)
        self.sync_scales()

        if name:
            self.stored['line'][name] = self.stored['line'].get(name,[])+[line[0]]

    def scatter(self,x,y,style=None):
        if not style: style = 'background'

        d = self.theme[self.current_theme][style]['scatter']
        self.axes['left'].scatter(x,y,**d)
        self.sync_scales()

    def render(self):
        plt.show(self.axes['left'])
