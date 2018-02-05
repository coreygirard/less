import matplotlib.pyplot as plt
import numpy as np
import structurer as telescope

#x=np.array([1,2,3,4,5])
#y=np.array([5,4,7,1,7])

np.random.seed(42)
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
y2 = y + 0.1 * np.random.normal(size=x.shape)



spine_properties = {'visible':'()',
                    'bounds':'()',
                    'ticks':'()'}
tree = {'plot':'()',
        'scatter':'()',
        'spine':{'left':spine_properties,
                 'right':spine_properties,
                 'top':spine_properties,
                 'bottom':spine_properties}}

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

        self.kill_all()

    def handle(self,route,*args,**kwargs):
        print(route,args,kwargs)

        if route[0] == 'spine':
            self.handle_spine(route[1:],args,kwargs)

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
            assert(type(args[0]) == list)
            self.ticks_lookup[spine](args[0])
            self.axes[spine].tick_params(**{spine:'on'})

            labels = kwargs.get('labels',False)
            if labels != False:
                if labels == 'auto':
                    self.labels_lookup[spine](args[0])
                else:
                    assert(type(labels) == list)
                    self.labels_lookup[spine](labels)

                self.axes[spine].tick_params(**{'label'+spine:'on'})

            leave_bounds = kwargs.get('leavebounds',False)
            if leave_bounds != True:
                self.spines_lookup[spine].set_bounds(min(args[0]),max(args[0]))





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
        self.axes['left'].plot(*args,**kwargs)
        self.sync_scales()

    def scatter(self,*args,**kwargs):
        self.axes['left'].scatter(*args,**kwargs)
        self.sync_scales()

    def render(self):
        plt.show(self.axes['left'])




chart = Chart(6,4)

mask = np.abs(y-y2) > 0.18
chart.plot(x, y, '--', color='#BBBBBB')

chart.scatter(x[mask], y2[mask], c='r', s=9)
chart.scatter(x[mask == False], y2[mask == False], c='grey', s=3)



chart.spine.right.visible(True)
chart.spine.left.visible(True)
chart.spine.right.bounds([-1,1])
chart.spine.right.ticks([-1,0.75,1],
                        labels='auto')
chart.spine.left.ticks([-1,-0.75,0.5],
                        labels=['red','green','blue'])

chart.render()










'''
#chart = Chart()

chart = Chart(6,4)



mask = np.abs(y-y2) > 0.18
chart.plot(x, y, '--', color='#BBBBBB')

chart.scatter(x[mask], y2[mask], c='r', s=9)
chart.scatter(x[mask == False], y2[mask == False], c='grey', s=3)

#chart.spine.left(visible=True,
#                 bounds=[-1,1])
chart.spine.left.visible(True)
chart.spine.left.bounds([-1,1])
chart.spine.left.ticks([-1,0,1],
                       ['red','green','blue'])

chart.spine.right.visible(True)
chart.spine.right.bounds([-1,1])
chart.spine.right.ticks([-1,0.75,1])

#chart.spine.left.visible(False)

chart.render()
'''









'''



ax.set_ylim((-1.25, 1.25))
ax.set_yticks([-1, 0, 1])

ax.spines['left'].set_color('#999999')
ax.tick_params(color='#999999')
ax.yaxis.set_ticks_position('both')

ax.tick_params(labeltop=False, labelright=True)

plt.show()
'''




'''
plt.tick_params(axis='both',
                which='both',
                bottom='on',
                top='off',
                labelbottom='on',
                left='off',
                right='off',
                labelleft='on',
                color=,
                length=)
'''
