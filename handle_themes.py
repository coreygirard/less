import json

class ThemesHandler(object):
    def __init__(self):
        with open('./themes/default.json', 'r') as f:
            self.data = json.load(f)

        self.data['jitter'] = {**self.data.get('scatter', {}),
                               **self.data.get('jitter', {})}

        self.default_theme = 'background'

    def apply(self, mode, args, kwargs):
        style = kwargs.pop('style', self.default_theme)

        theme = self.data.get(mode, {})
        theme = theme.get(style, {})

        kwargs = {**theme, **kwargs}

        return args, kwargs



'''
th = ThemesHandler()

def f(*args, **kwargs):
    mode = 'scatter'

    args, kwargs = th.apply(mode, args, kwargs)
    print(args, kwargs)

f(style='highlight')
'''
