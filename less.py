import matplotlib.pyplot as plt
import numpy as np
import os
from pprint import pprint
import json
import structurer as telescope


spine_properties = {'visible':'()',
                    'bounds':'()',
                    'ticks':'()',
                    'ticks_minor':'()'}
tree = {'plot':'()',
        'scatter':'()',
        'xlim':'()',
        'ylim':'()',
        'spine':{'left':spine_properties,
                 'right':spine_properties,
                 'top':spine_properties,
                 'bottom':spine_properties}}

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

        self._telescope = telescope.Telescope(tree,self.handle)

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
        #print(route,args,kwargs)

        head,tail = route[0],route[1:]

        if head == 'spine':
            self.handle_spine(tail,args,kwargs)
        elif head == 'xlim':
            self.handle_xlim(tail,args,kwargs)
        elif head == 'ylim':
            self.handle_ylim(tail,args,kwargs)

    def handle_spine(self,route,args,kwargs):
        assert(len(route) == 2)
        assert(route[0] in self.spines_lookup.keys())

        spine,cmd = route

        if cmd == 'visible':
            assert(args[0] in [True,False])
            self.spines_lookup[spine].set_visible(args[0])
        elif cmd == 'bounds':
            assert(len(args[0]) == 2)
            self.spines_lookup[spine].set_bounds(*args[0])
        elif cmd == 'ticks':
            self.handle_spine_ticks(spine,cmd,args,kwargs)
        elif cmd == 'ticks_minor':
            self.handle_spine_ticks_minor(spine,cmd,args,kwargs)

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
        self.axes['left'].set_ylim(*args[0])
        self.sync_scales()

    def handle_xlim(self,route,args,kwargs):
        self.axes['left'].set_xlim(*args[0])
        self.sync_scales()

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

    def plot(self,x,y,style=None):
        if not style: style = 'background'

        d = self.theme[self.current_theme][style]['plot']
        self.axes['left'].plot(x,y,'--',**d)
        self.sync_scales()

    def scatter(self,x,y,style=None):
        if not style: style = 'background'

        d = self.theme[self.current_theme][style]['scatter']
        self.axes['left'].scatter(x,y,**d)
        self.sync_scales()

    '''
    def plot(self,*args,**kwargs):
        self.axes['left'].plot(*args,**kwargs)
        self.sync_scales()

    def scatter(self,*args,**kwargs):
        self.axes['left'].scatter(*args,**kwargs)
        self.sync_scales()
    '''

    def render(self):
        plt.show(self.axes['left'])


np.random.seed(42)

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)

y2 = y + 0.1 * np.random.normal(size=x.shape)
mask = np.abs(y-y2) > 0.18

# tweak one point to be better within bounds
i = [i for i,e in enumerate(mask) if e][-1]
y2[i] += 2*(y[i]-y2[i])


chart = Chart(6,4)

chart.plot(x, y)

chart.scatter(x[mask], y2[mask], style='highlight')
chart.scatter(x[mask == False], y2[mask == False], style='background')

chart.spine.left.visible(True)
chart.spine.left.ticks([-1,0,1])
chart.spine.left.ticks_minor(y2[mask])

chart.spine.right.visible(True)
chart.spine.right.ticks([-1,0,1])
chart.spine.right.ticks_minor(y2[mask])

chart.spine.bottom.ticks([0, np.pi, 2*np.pi],
                         labels=['0', '$\pi$', '2$\pi$'])
chart.spine.bottom.ticks_minor(x[mask])

chart.xlim((-0.1, 2*np.pi+0.1))
chart.ylim((-1.25,1.25))

chart.render()
