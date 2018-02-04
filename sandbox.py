import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
y2 = y + 0.1 * np.random.normal(size=x.shape)


'''
class TicksHandler(object):
    def __init__(self, ax):
        self.ax = ax

    def visible(self, s, prop):
        self.ax.tick_params(**{s:['off','on'][prop]})

class LabelsHandler(object):
    def __init__(self, ax):
        self.ax = ax

    def visible(self, s, prop):
        self.ax.tick_params(**{'label'+s:['off','on'][prop]})
'''
class SpineHandler(object):
    def __init__(self, ax):
        self.ax = ax

    def visible(self, s, prop):
        self.ax.spines[s].set_visible(prop)

    def __getattr__(self,e):
        if e == 'ticks':
            return TicksHandler(self.ax)
        elif e == 'labels':
            return LabelsHandler(self.ax)


class Chart(object):
    def __init__(self,x=6,y=6):
        self.fig = plt.figure(figsize=(x,y))
        self.ax = self.fig.subplots()

        self.kill_all()

    def render(self):
        plt.show(self.ax)

    def kill_all(self):
        for s in ['top','bottom','left','right']:
            self.spine.visible(s,False)
            self.spine.ticks.visible(s,False)
            self.spine.labels.visible(s,False)

    def __getattr__(self,e):
        if e == 'spine':
            return SpineHandler(self.ax)
        else:
            return None

    '''

    def spine_left_ticks_off(self,ax):
        self.ax.tick_params(left='off')

    def spine_left_ticks_on(self,ax):
        self.ax.tick_params(left='on')

    def spine_left_labels_off(self,ax):
        self.ax.tick_params(labelleft='off')

    def spine_left_labels_on(self,ax):
        self.ax.tick_params(labelleft='on')

    def spine_left_kill(self,ax):
        self.spine_left_ticks_off(ax)
        self.spine_left_labels_off(ax)
        self.spine_left_visible(False)

    def spine_left_bounds_set(self,ymin=None,ymax=None):
        if ymin != None and ymax != None:
            self.ax.spines['left'].set_bounds(ymin,ymax)
        elif ymin != None:
            _,ymax = self.ax.spines['left'].get_bounds()
            self.ax.spines['left'].set_bounds(ymin,ymax)
        elif ymax != None:
            ymin,_ = self.ax.spines['left'].get_bounds()
            self.ax.spines['left'].set_bounds(ymin,ymax)
    '''

    def plot(self,*args,**kwargs):
        self.ax.plot(*args,**kwargs)

    def scatter(self,*args,**kwargs):
        self.ax.scatter(*args,**kwargs)



#x=np.array([1,2,3,4,5])
#y=np.array([5,4,7,1,7])


#chart = Chart()
#chart.plot(x,y,'ok')
#chart.spine_left_bounds_set(2,5)
#chart.render()

chart = Chart(6,4)



mask = np.abs(y-y2) > 0.18
chart.plot(x, y, '--', color='#BBBBBB')

chart.scatter(x[mask], y2[mask], c='r', s=9)
chart.scatter(x[mask == False], y2[mask == False], c='grey', s=3)

#chart.spine.visible('left',True)
#chart.spine.visible('right',True)
chart.spine.left(visible=True)

chart.render()

'''


ax.set_xlim((0-0.1, 2*np.pi+0.1))
ax.set_xticks([0, np.pi, 2*np.pi])
ax.set_xticks(x[mask],minor=True)
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
