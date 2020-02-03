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

def _bar_get_data(kwargs):
    categories = kwargs.pop('categories')
    values = kwargs.pop('values')

    assert isinstance(categories, list)
    assert isinstance(values, list)

    return categories, values

def _bar_set_borders(bar):
    for p in bar:
        #if False: #label in highlight:
        #    p.set_color('#F79646')
        #else:
        #    p.set_color('#E0E0E0')

        p.set_edgecolor('white')
        p.set_linewidth(3)

def _hbar_convert_to_all_lists(values):
    output = []
    for e in values:
        if isinstance(e, list):
            output.append(e)
        else:
            output.append([e])

    return output

def vbar(ax, *args, **kwargs):
    categories, values = _bar_get_data(kwargs)

    #if any(map(lambda x: type(x) == str, x)):
    #    x = list(range(len(x)))

    #name = kwargs.pop('name', None)

    bar = ax.get_primary_axes().bar(categories, values, **kwargs)
    ax.sync_scales()

    #if name:
    #    if name not in self.parent.stored.keys():
    #        self.parent.stored[name] = elements.Iterator()
    #    self.parent.stored[name].add(elements.VerticalBarChartObject(bar))



def hbar(ax, *args, **kwargs):
    categories, values = _bar_get_data(kwargs)

    start = kwargs.pop('start', None)
    assert start in ['top', 'bottom', None]

    if start is None and any(map(lambda i: isinstance(i, str), values)):
        start = 'bottom'

    if start == 'bottom':
        categories = list(reversed(range(len(categories))))

    left = np.zeros((len(values),))

    if not isinstance(values[0], list):
        values = [[i] for i in values]

    for e in zip(*values):
        print(e)
        bar = ax.get_primary_axes().barh(categories, e, left=left, **kwargs)
        left += np.array(e)

        _bar_set_borders(bar)


    #name = kwargs.pop('name', None)

    #bar = ax.get_primary_axes().barh(categories, values, **kwargs)

    #ymin, ymax = self.get_axes().get_ylim()
    #self.get_axes().set_ylim(ymax, ymin)

    ax.sync_scales()

    #if name:
    #    if name not in self.parent.stored.keys():
    #        self.parent.stored[name] = elements.Iterator()
    #    self.parent.stored[name].add(elements.HorizontalBarChartObject(bar))

def cake(ax, *args, **kwargs):
    cat = kwargs.get('categories', None)
    mag = kwargs.get('values', None)

    highlight = kwargs.get('highlight', [])

    width = 1

    #highlight_color = '#F79646'
    #background_color = '#bbbbbb'
    for i in range(len(mag)):
        bottom = sum(mag[:i]) / sum(mag)
        height = mag[i] / sum(mag)

        if cat[i] in highlight:
            color = kwargs.get('color') #highlight_color
        else:
            color = kwargs.get('color') #background_color

        bar = ax.get_primary_axes().bar(0, height, bottom=bottom, width=width, color=color)
        for p in bar.patches:
            # sets outline to same color as background. Hackjob for transparency
            p.set_edgecolor(ax.get_primary_axes().get_facecolor())
            p.set_linewidth(kwargs.get('linewidth'))

        #plt.text(0, bottom+height/2, cat[i], ha='center', va='center', color='white', fontsize=16)

def background(ax, *args, **kwargs):
    print('background', ax, args, kwargs)

    color = kwargs.pop('color', None)
    alpha = kwargs.pop('alpha', None)

    ax = ax.get_primary_axes()

    contains_x = any(['xlim' in kwargs.keys(),
                      'xmin' in kwargs.keys(),
                      'xmax' in kwargs.keys()])
    contains_y = any(['ylim' in kwargs.keys(),
                      'ymin' in kwargs.keys(),
                      'ymax' in kwargs.keys()])

    assert not (contains_x and contains_y)

    if 'xlim' in kwargs.keys():
        xmin, xmax = kwargs['xlim']
    else:
        xmin = kwargs.get('xmin', ax.get_xlim()[0])
        xmax = kwargs.get('xmax', ax.get_xlim()[1])

    if 'ylim' in kwargs.keys():
        ymin, ymax = kwargs['ylim']
    else:
        ymin = kwargs.get('ymin', ax.get_ylim()[0])
        ymax = kwargs.get('ymax', ax.get_ylim()[1])

    kw = {'facecolor': color,
          'alpha': alpha}


    print(xmin, xmax, ymin, ymax)
    if (ymin is None) and (ymax is None):
        if not xmin is None:
            kw['xmin'] = xmin
        else:
            kw['xmin'] = ax.get_xlim()[0]

        if not xmax is None:
            kw['xmax'] = xmin
        else:
            kw['xmax'] = ax.get_xlim()[1]

        ax.axvspan(**kw)

    if (xmin is None) and (xmax is None) and \
       (not ymin is None) and (not ymax is None):
        ax.axhspan(ymin=ymin, ymax=ymax, facecolor=color, alpha=alpha)



    '''
    xlim = kwargs.pop('xlim', None)
    if xlim:
        ax.axvspan(*xlim, facecolor=color, alpha=0.5)

    ylim = kwargs.pop('ylim', None)
    if ylim:
        ax.axhspan(*ylim, facecolor=color, alpha=0.5)

    xmin = kwargs.pop('xmin', None)
    if xmin:
        ax.axvspan(xmin=xmin, xmax=, facecolor=color, alpha=0.5)

    xmax = kwargs.pop('xmax', None)
    if xmax:
        ax.axvspan(xmin=, xmax=xmax, facecolor=color, alpha=0.5)

    ymin = kwargs.pop('ymin', None)
    if ymin:
        ax.axhspan(ymin=ymin, ymax=ax.get_ylim()[1], facecolor=color, alpha=0.5)

    ymax = kwargs.pop('ymax', None)
    if ymax:
        ax.axhspan(ymin=ax.get_ylim()[0], ymax=ymax, facecolor=color, alpha=0.5)
    '''
