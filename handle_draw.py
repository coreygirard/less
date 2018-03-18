import numpy as np
import handle_elements as elements


def merge_themes(theme, kwargs):
    theme = {**theme, **kwargs}
    return theme

class Draw(object):
    def get_axes(self):
        return self.parent.axes.axes['left']

    def plot(self, *args, **kwargs):
        # require x and y as kwargs
        assert len(args) == 0

        style = kwargs.pop('style', 'background')
        theme = self.parent.get_current_theme(style, 'plot')

        theme = merge_themes(theme, kwargs)

        name = theme.pop('name', None)
        x = theme.pop('x', None)
        y = theme.pop('y', None)

        line = self.get_axes().plot(x, y, **theme)
        self.sync_scales()

        if name:
            if name not in self.parent.stored.keys():
                self.parent.stored[name] = elements.Iterator()
            self.parent.stored[name].add(elements.LineObject(line[0]))

    def scatter(self, x, y, **kwargs):
        style = kwargs.get('style', 'background')

        theme = self.parent.get_current_theme(style, 'scatter')
        self.get_axes().scatter(x, y, **theme)
        self.sync_scales()

    def jitter(self, *args, **kwargs):
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

    def vbar(self, *args, **kwargs):
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

    def hbar(self, *args, **kwargs):
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
