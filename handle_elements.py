import matplotlib


class Iterator(object):
    def __init__(self):
        self.v = []

    def add(self, e):
        self.v.append(e)

    def label(self, *args, **kwargs):
        for e in self.v:
            e.label(*args, **kwargs)


class LineObject(object):
    def __init__(self, line):
        self.line = line

    def get_end_xy(self, end):
        x1, y1, x2, y2 = (self.line.get_xdata()[0],
                          self.line.get_ydata()[0],
                          self.line.get_xdata()[-1],
                          self.line.get_ydata()[-1])

        fudge = 0.1

        if end == 'left':
            if x1 > x2:
                return x2-fudge, y2
            else:
                return x1-fudge, y1
        elif end == 'right':
            if x1 > x2:
                return x1+fudge, y1
            else:
                return x2+fudge, y2

    def get_alignments(self, end):
        if end == 'left':
            h, v = 'right', 'center'
        elif end == 'right':
            h, v = 'left', 'center'

        return h, v

    def label(self, text, end='right'):
        x, y = self.get_end_xy(end)
        h, v = self.get_alignments(end)

        self.line.axes.text(x, y, text,
                            fontsize=12,
                            color=self.line.get_color(),
                            horizontalalignment=h,
                            verticalalignment=v)

class VerticalBarChartObject(object):
    def __init__(self, bar):
        self.bar = bar

    def label(self, *args, **kwargs):
        loc = kwargs.pop('loc')
        inside = kwargs.pop('inside', True)
        parse = kwargs.pop('parse', None)

        kwargs['horizontalalignment'] = kwargs.get('horizontalalignment', 'center')
        kwargs['verticalalignment'] = kwargs.get('verticalalignment', 'center')

        for r in self.bar:
            h = r.get_height()
            if parse:
                h = parse(h)

            # get coords of bar center
            x = r.get_x() + r.get_width()/2
            y = r.get_y() + r.get_height()/2

            # adjust to top or bottom if necessary
            if loc == 'top':
                y += r.get_height()/2
            elif loc == 'bottom':
                y -= r.get_height()/2

            # calculate offset in units of font points
            fontsize = kwargs.get('fontsize')
            offset = fontsize * 1.0
            if (loc == 'top' and inside) or (loc == 'bottom' and not inside):
                offset *= -1

            r.axes.annotate(h,
                            xy=(x, y), xycoords='data',
                            xytext=(0, offset), textcoords='offset points',
                            **kwargs)

class HorizontalBarChartObject(object):
    def __init__(self, bar):
        self.bar = bar

    def label(self, *args, **kwargs):
        loc = kwargs.pop('loc')
        inside = kwargs.pop('inside', True)
        parse = kwargs.pop('parse', None)

        kwargs['horizontalalignment'] = kwargs.get('horizontalalignment', 'center')
        kwargs['verticalalignment'] = kwargs.get('verticalalignment', 'center')

        for r in self.bar:
            w = r.get_width()
            if parse:
                w = parse(w)

            # get coords of bar center
            x = r.get_x() + r.get_width()/2
            y = r.get_y() + r.get_height()/2

            # calculate offset in units of font points
            fontsize = kwargs.get('fontsize')
            offset = fontsize * 0.5

            # adjust to top or bottom if necessary
            if loc == 'left' and not inside:
                x -= r.get_width()/2
                offset *= -1
                kwargs['horizontalalignment'] = 'right'

            elif loc == 'left' and inside:
                x -= r.get_width()/2
                kwargs['horizontalalignment'] = 'left'

            elif loc == 'center':
                pass

            elif loc == 'right' and inside:
                x += r.get_width()/2
                offset *= -1
                kwargs['horizontalalignment'] = 'right'

            elif loc == 'right' and not inside:
                x += r.get_width()/2
                kwargs['horizontalalignment'] = 'left'

            r.axes.annotate(w,
                            xy=(x, y), xycoords='data',
                            xytext=(offset, 0), textcoords='offset points',
                            **kwargs)

'''
def wrap(e, typ):
    if typ == 'line'
        return Iterator([LineObject(i) for i in e])

    if typ == 'vbar':
        return Iterator([VerticalBarChartObject(i) for i in e])
'''
