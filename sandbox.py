import matplotlib.pyplot as plt
import numpy as np

#x=np.array([1,2,3,4,5])
#y=np.array([5,4,7,1,7])

np.random.seed(42)
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
y2 = y + 0.1 * np.random.normal(size=x.shape)


class SpineHandler(object):
    def __init__(self,spine,ax):
        self.spine = spine
        self.ax = ax

    def __call__(self,*args,**kwargs):
        visible = kwargs.get('visible',None)
        if visible in [False,True]:
            self.visible(visible)

        bounds = kwargs.get('bounds',None)
        if bounds != None:
            self.bounds(bounds)

    def visible(self,b):
        self.spine.set_visible(b)

    def bounds(self,bounds):
        assert(len(bounds) == 2)
        self.spine.set_bounds(bounds[0],bounds[1])

    def ticks(self,ticks,labels=None):
        self.ax.set_yticks(ticks)
        if labels:
            self.ax.set_yticklabels(labels)

class SpinesHandler(object):
    def __init__(self, chart):
        self.chart = chart

    def __getattr__(self,e):
        if e == 'left':
            return SpineHandler(self.chart.ax_left.spines['left'],
                                self.chart.ax_left)
        elif e == 'right':
            return SpineHandler(self.chart.ax_right.spines['right'],
                                self.chart.ax_right)
        elif e == 'top':
            return SpineHandler(self.chart.ax_top.spines['top'],
                                self.chart.ax_top)
        elif e == 'bottom':
            return SpineHandler(self.chart.ax_bottom.spines['bottom'],
                                self.chart.ax_bottom)


class Chart(object):
    def __init__(self,x=6,y=6):
        self.fig = plt.figure(figsize=(x,y))

        self.ax_left = self.fig.subplots()
        self.ax_right = self.ax_left.twinx()

        self.ax_top = self.ax_left.twiny()
        self.ax_bottom = self.ax_top.twiny()

        self.ax_left.yaxis.set_ticks_position('left')
        self.ax_right.yaxis.set_ticks_position('right')
        self.ax_top.xaxis.set_ticks_position('top')
        self.ax_bottom.xaxis.set_ticks_position('bottom')

        self.kill_all()

    def render(self):
        plt.show(self.ax)

    def kill_all(self):
        #self.spine.left(visible=False)

        for axes in [self.ax_left,
                     self.ax_right,
                     self.ax_top,
                     self.ax_bottom]:

            params = {}
            for k in ['left','right','top','bottom']:
                params[k] = 'off'
                params['label'+k] = 'off'
            axes.tick_params(axis='both',**params)
            for s in ['top','bottom','left','right']:
                axes.spines[s].set_visible(False)

    def __getattr__(self,e):
        if e == 'spine':
            return SpinesHandler(self)
        else:
            return None

    def plot(self,*args,**kwargs):
        self.ax_left.plot(*args,**kwargs)

        self.ax_right.set_ylim(*self.ax_left.get_ylim())
        self.ax_top.set_xlim(*self.ax_left.get_xlim())
        self.ax_bottom.set_xlim(*self.ax_left.get_xlim())


    def scatter(self,*args,**kwargs):
        self.ax_left.scatter(*args,**kwargs)




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
