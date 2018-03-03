import numpy as np


class Draw(object):
    def plot(self, *args, **kwargs):
        assert(len(args) == 0)

        if 'style' not in kwargs: kwargs['style'] = 'background'

        theme = self.parent.get_current_theme()[kwargs['style']]['plot']

        for k in ['color','linestyle']:
            if k in kwargs:
                theme[k] = kwargs[k]

        name = kwargs.pop('name', None)
        axes = self.parent.axes.axes['left']
        line = axes.plot(kwargs['x'], kwargs['y'], **theme)
        self.sync_scales()

        if name:
            if 'line' not in self.parent.stored.keys():
                self.parent.stored['line'] = {}
            if name not in self.parent.stored['line'].keys():
                self.parent.stored['line'][name] = []
            self.parent.stored['line'][name].append(line[0])

    def scatter(self, x, y, **kwargs):
        style = kwargs.get('style', 'background')

        theme = self.parent.get_current_theme()[style]['scatter']
        axes = self.parent.axes.axes['left']
        axes.scatter(x,y,**theme)
        self.sync_scales()

    def jitter(self, *args, **kwargs):
        x_width = kwargs.pop('x_width', None)
        y_width = kwargs.pop('y_width', None)

        x = kwargs.pop('x')
        y = kwargs.pop('y')

        x_ = x + np.random.random(x.shape)*x_width - (x_width/2) if x_width else x

        if y_width:
            y_ = y + np.random.random(y.shape)*y_width - (y_width/2)
        else:
            y_ = y

        self.scatter(x_, y_, **kwargs)
