import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint


class Chart(object):
    def __init__(self):
        self.fig, self.ax = plt.subplots()

        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.spines = ['top',
                       'bottom',
                       'left',
                       'right']

        self.lookup = {}

    def set_visible_spines(self,s):
        for i in self.spines:
            self.ax.spines[i].set_visible(i in s)

    def plot_set_background(self,*args,**kwargs):
        if 'plot' not in self.lookup.keys():
            self.lookup['plot'] = {}
        self.lookup['plot']['background'] = kwargs
        pprint(self.lookup)




    def set_ticks(self,*args,**kwargs):
        for s in self.spines:
            if s in kwargs.keys():
                if not (s+'_loc' in kwargs.keys() and s+'_label' in kwargs.keys()):
                    kwargs[s+'_loc'] = kwargs[s]
                    kwargs[s+'_label'] = kwargs[s]
                    del kwargs[s]

        if 'left_loc' in kwargs.keys() and 'left_label' in kwargs.keys():
            self.ax.set_yticks(kwargs['left_loc'])
            self.ax.set_yticklabels(kwargs['left_label'])
            self.ax.spines['left'].set_bounds(min(kwargs['left_loc']),
                                              max(kwargs['left_loc']))

        if 'bottom_loc' in kwargs.keys() and 'bottom_label' in kwargs.keys():
            self.ax.set_xticks(kwargs['bottom_loc'])
            self.ax.set_xticklabels(kwargs['bottom_label'])
            self.ax.spines['bottom'].set_bounds(min(kwargs['bottom_loc']),
                                                max(kwargs['bottom_loc']))

    def scatter(self,*args,**kwargs):
        defaults = {'c':'grey',
                    's':9}
        for k,v in defaults.items():
            if k not in kwargs:
                kwargs[k] = v

        self.ax.scatter(*args,**kwargs)

    def plot(self,*args,**kwargs):
        defaults = {'linestyle':'--',
                    'color':'#BBBBBB'}
        for k,v in defaults.items():
            if k not in kwargs:
                kwargs[k] = v

        self.ax.plot(*args,**kwargs)

    def render(self):
        plt.show(self.fig)

'''
mask = np.abs(y-y2) > 0.15
ax.plot(x, y, '--', color='#BBBBBB')
ax.scatter(x[mask], y2[mask], c='r', s=9)
ax.scatter(x[mask == False], y2[mask == False], c='grey', s=3)

ax.set_xlim((0-0.1, 2*np.pi+0.1))
ax.set_xticks([0, np.pi, 2*np.pi])
ax.set_xticklabels(['0', '$\pi$', '2$\pi$'])
ax.spines['bottom'].set_bounds(0,2*np.pi)
ax.xaxis.set_ticks_position('bottom')


ax.set_ylim((-1.25, 1.25))
ax.set_yticks([-1, 0, 1])
ax.spines['left'].set_bounds(-1, 1)
ax.spines['right'].set_bounds(-1, 1)

ax.spines['left'].set_color('#999999')
ax.spines['right'].set_color('#999999')
ax.tick_params(color='#999999')
ax.yaxis.set_ticks_position('both')

ax.tick_params(labeltop=False, labelright=True)

plt.show()
'''
