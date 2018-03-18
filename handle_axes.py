import matplotlib.pyplot as plt
import handle_draw as draw

class Axes(draw.Draw):
    def __init__(self, x, y, parent):
        self.parent = parent

        self.fig = plt.figure(figsize=(x, y))

        self.create_axes()
        self.init_ticks_position()
        self.init_label_position()
        self.init_lookup()
        self.kill_chartjunk()

    def create_axes(self):
        self.axes = {}
        self.axes['left'] = self.fig.subplots()
        self.axes['right'] = self.axes['left'].twinx()
        self.axes['top'] = self.axes['left'].twiny()
        self.axes['bottom'] = self.axes['top'].twiny()

    def init_ticks_position(self):
        self.axes['left'].yaxis.set_ticks_position('left')
        self.axes['right'].yaxis.set_ticks_position('right')
        self.axes['top'].xaxis.set_ticks_position('top')
        self.axes['bottom'].xaxis.set_ticks_position('bottom')

    def init_label_position(self):
        self.axes['left'].yaxis.set_label_position('left')
        self.axes['right'].yaxis.set_label_position('right')
        self.axes['top'].xaxis.set_label_position('top')
        self.axes['bottom'].xaxis.set_label_position('bottom')

    def init_lookup(self):
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

    def sync_scales(self):
        self.axes['right'].set_ylim(*self.axes['left'].get_ylim())
        self.axes['top'].set_xlim(*self.axes['left'].get_xlim())
        self.axes['bottom'].set_xlim(*self.axes['left'].get_xlim())

    def set_axis_label(self, spine, args, kwargs):
        if spine == 'left':
            self.axes['left'].set_ylabel(args[0])
        elif spine == 'right':
            self.axes['right'].set_ylabel(args[0])
        elif spine == 'top':
            self.axes['top'].set_xlabel(args[0])
        elif spine == 'bottom':
            self.axes['bottom'].set_xlabel(args[0])

    def kill_chartjunk(self):
        for axes in [self.axes['left'],
                     self.axes['right'],
                     self.axes['top'],
                     self.axes['bottom']]:

            params = {}
            for k in ['left', 'right', 'top', 'bottom']:
                params[k] = 'off'
                params['label'+k] = 'off'
            axes.tick_params(axis='both', **params)
            for s in ['top', 'bottom', 'left', 'right']:
                axes.spines[s].set_visible(False)

    def handle(self, route):
        head = route.pop(0)

        if head.val in ['plot',
                        'scatter',
                        'jitter',
                        'vbar',
                        'hbar']:
            assert head.type == '()'
            getattr(self, head.val)(*head.args, **head.kwargs)
        elif head.val == 'spine' and head.type == 'attr':
            self.handle_spine(route)
        elif head.val == 'xlim' and head.type == '()':
            self.handle_xlim(head.args)
        elif head.val == 'ylim' and head.type == '()':
            self.handle_ylim(head.args)
        elif head.val == 'line' and head.type == '[]':
            self.handle_line(route)
        elif head.val == 'title' and head.type == '()':
            self.axes['left'].set_title(*head.args, **head.kwargs)
        else:
            print('unknown command:', head, route)

    def handle_spine(self, route):
        spine = route.pop(0).val
        assert spine in self.spines_lookup.keys()

        cmd = route[0].val

        if cmd == 'visible':
            self.spines_lookup[spine].set_visible(route[0].args[0])
        elif cmd == 'bounds':
            self.spines_lookup[spine].set_bounds(*route[0].args[0])
        elif cmd == 'ticks':
            self.handle_spine_ticks(spine, route[1])
        #elif cmd == ['label()']:
        #    self.set_axis_label(spine, args, kwargs)

    def handle_spine_ticks(self, spine, cmd):
        if cmd.val == 'major':
            self.handle_spine_ticks_major(spine, cmd)

        elif cmd.val == 'minor':
            self.handle_spine_ticks_minor(spine, cmd)

    def handle_spine_ticks_major(self, spine, cmd):
        labels = cmd.kwargs.get('labels',False)
        labelsize = cmd.kwargs.get('fontsize', None)
        try:
            n = cmd.args[0]
        except:
            n = list(range(len(labels)))

        # sets the tick locations themselves (iirc)
        self.ticks_lookup[spine](n)

        # sets properties of the ticks
        params = {spine:'on'}
        if labelsize:
            params['labelsize'] = labelsize
        self.axes[spine].tick_params(**params)

        if labels == False:
            self.labels_lookup[spine](cmd.args[0])
        else:
            assert(type(labels) == list)
            self.labels_lookup[spine](labels)

        # makes sure labels are visible
        self.axes[spine].tick_params(**{'label' + spine:'on'})

        leave_bounds = cmd.kwargs.get('leavebounds', False)
        if leave_bounds != True:
            self.spines_lookup[spine].set_bounds(min(n), max(n))

    def handle_spine_ticks_minor(self, spine, cmd):
        self.ticks_lookup[spine](cmd.args[0], minor=True)

    def handle_xlim(self, args):
        self.axes['left'].set_xlim(*args)
        self.sync_scales()

    def handle_ylim(self, args):
        self.axes['left'].set_ylim(*args)
        self.sync_scales()

    '''
    def handle_line(self,route,args,kwargs):
        if route == ['label()']:
            self.handle_line_label(args,kwargs)

    def handle_line_label(self,args,kwargs):
        for line in self.stored['line'][kwargs['line']]:
            x,y = line.get_xydata()[-1]
            color = kwargs.get('color',line.get_color())
            self.axes['left'].text(x+0.1,y,
                                   kwargs['label'],
                                   verticalalignment='center',
                                   color=color)
    '''

    def render(self):
        plt.show(self.axes['left'])
