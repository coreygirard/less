class ThemesHandler(object):
    def __init__(self):
        pass

    def apply_plot(self, args, kwargs):
        return args, kwargs

    def apply(self, mode, args, kwargs):
        return getattr(self, f'apply_{mode}')(args, kwargs)
