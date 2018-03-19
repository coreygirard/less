import numpy as np
import handle_elements as elements

# plt.hexbin
# plt.hist
# plt.hist2d
# plt.imshow   # for heatmaps
# plt.stem
# plt.step
# plt.hex
# plt.stream
# plt.table
# plt.violin

# plt.xscale / plt.yscale



#def merge_themes(theme, kwargs):
#    theme = {**theme, **kwargs}
#    return theme




def plot(ax, *args, **kwargs):
    # add ability for loglog, semilogy, semilogx via kwargs
    # handle dates via kwargs? (matplotlib.pyplot.plot_date)


    # require x and y as kwargs
    #assert len(args) == 0

    #style = kwargs.pop('style', 'background')
    #theme = self.parent.get_current_theme(style, 'plot')

    #theme = merge_themes(theme, kwargs)

    #name = theme.pop('name', None)

    x = kwargs.pop('x', None)
    y = kwargs.pop('y', None)

    if isinstance(x, list):
        x = np.array(x)
    if isinstance(y, list):
        y = np.array(y)

    line = ax.get_primary_axes().plot(x, y, **kwargs)
    ax.sync_scales()

    #if name:
    #    if name not in self.parent.stored.keys():
    #        self.parent.stored[name] = elements.Iterator()
    #    self.parent.stored[name].add(elements.LineObject(line[0]))

def scatter(ax, *args, **kwargs):
    #style = kwargs.get('style', 'background')
    kwargs.pop('style', None)

    #theme = self.parent.get_current_theme(style, 'scatter')

    x = kwargs.pop('x', None)
    y = kwargs.pop('y', None)

    if isinstance(x, list):
        x = np.array(x)
    if isinstance(y, list):
        y = np.array(y)

    ax.get_primary_axes().scatter(x, y, **kwargs)
    ax.sync_scales()

def jitter(ax, *args, **kwargs):
    x_width = kwargs.pop('x_width', 0)
    y_width = kwargs.pop('y_width', 0)

    x = kwargs['x']
    y = kwargs['y']

    if isinstance(x, list):
        x = np.array(x)
    if isinstance(y, list):
        y = np.array(y)

    x_jitter = np.random.random(x.shape)*x_width - (x_width/2)
    y_jitter = np.random.random(y.shape)*y_width - (y_width/2)

    kwargs['x'] = x + x_jitter
    kwargs['y'] = y + y_jitter

    scatter(ax, *args, **kwargs)

def vbar(ax, *args, **kwargs):
    x = kwargs.pop('x')
    y = kwargs.pop('y')

    if isinstance(x, list):
        x = np.array(x)
    if isinstance(y, list):
        y = np.array(y)

    #if any(map(lambda x: type(x) == str, x)):
    #    x = list(range(len(x)))

    #name = kwargs.pop('name', None)

    bar = ax.get_primary_axes().bar(x, y, **kwargs)
    ax.sync_scales()

    #if name:
    #    if name not in self.parent.stored.keys():
    #        self.parent.stored[name] = elements.Iterator()
    #    self.parent.stored[name].add(elements.VerticalBarChartObject(bar))

def hbar(ax, *args, **kwargs):
    y = kwargs.pop('y')
    x = kwargs.pop('x')

    if isinstance(x, list):
        x = np.array(x)
    if isinstance(y, list):
        y = np.array(y)

    if any(map(lambda i: isinstance(i, str), x)):
        y = list(reversed(range(len(y))))

    #name = kwargs.pop('name', None)

    bar = ax.get_primary_axes().barh(y, x, **kwargs)

    #ymin, ymax = self.get_axes().get_ylim()
    #self.get_axes().set_ylim(ymax, ymin)

    ax.sync_scales()

    #if name:
    #    if name not in self.parent.stored.keys():
    #        self.parent.stored[name] = elements.Iterator()
    #    self.parent.stored[name].add(elements.HorizontalBarChartObject(bar))
