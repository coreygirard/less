import numpy as np
import handle_elements as elements




#def merge_themes(theme, kwargs):
#    theme = {**theme, **kwargs}
#    return theme




def plot(ax, *args, **kwargs):
    # require x and y as kwargs
    #assert len(args) == 0

    #style = kwargs.pop('style', 'background')
    #theme = self.parent.get_current_theme(style, 'plot')

    #theme = merge_themes(theme, kwargs)

    #name = theme.pop('name', None)

    x = kwargs.pop('x', None)
    y = kwargs.pop('y', None)


    line = ax.get_primary_axes().plot(x, y, **kwargs)
    ax.sync_scales()

    #if name:
    #    if name not in self.parent.stored.keys():
    #        self.parent.stored[name] = elements.Iterator()
    #    self.parent.stored[name].add(elements.LineObject(line[0]))

def scatter(ax, *args, **kwargs):
    #style = kwargs.get('style', 'background')
    kwargs.pop('style')

    #theme = self.parent.get_current_theme(style, 'scatter')

    x = kwargs.pop('x', None)
    y = kwargs.pop('y', None)

    ax.get_primary_axes().scatter(x, y, **kwargs)
    ax.sync_scales()

def jitter(ax, *args, **kwargs):
    x_width = kwargs.pop('x_width', None)
    y_width = kwargs.pop('y_width', None)

    x = kwargs.pop('x')
    y = kwargs.pop('y')

    if x_width:
        x_ = x + np.random.random(x.shape)*x_width - (x_width/2)
    else:
        x_ = x

    if y_width:
        y_ = y + np.random.random(y.shape)*y_width - (y_width/2)
    else:
        y_ = y

    self.scatter(x_, y_, **kwargs)

def vbar(ax, *args, **kwargs):
    x = kwargs.pop('x')
    y = kwargs.pop('y')

    if any(map(lambda x: type(x) == str, x)):
        x = list(range(len(x)))

    name = kwargs.pop('name', None)

    bar = self.get_axes().bar(x, y, **kwargs)
    self.sync_scales()

    if name:
        if name not in self.parent.stored.keys():
            self.parent.stored[name] = elements.Iterator()
        self.parent.stored[name].add(elements.VerticalBarChartObject(bar))

def hbar(ax, *args, **kwargs):
    y = kwargs.pop('y')
    x = kwargs.pop('x')

    if True: #any(map(lambda x: type(x) == str, x)):
        y = list(range(len(y)))

    name = kwargs.pop('name', None)

    bar = self.get_axes().barh(y, x, **kwargs)

    ymin, ymax = self.get_axes().get_ylim()
    self.get_axes().set_ylim(ymax, ymin)

    self.sync_scales()

    if name:
        if name not in self.parent.stored.keys():
            self.parent.stored[name] = elements.Iterator()
        self.parent.stored[name].add(elements.HorizontalBarChartObject(bar))
