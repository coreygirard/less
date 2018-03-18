import foldr
from collections import namedtuple


Node = namedtuple('Node', 'type val args kwargs')


def convert_tree(tree):
    if isinstance(tree, str):
        return {tree: None}

    d = {}
    for k, v in tree:
        if k.startswith('.'):
            if '.' not in d:
                d['.'] = {}

            k = k.lstrip('.')
            if k.endswith('()'):
                k = k[:-2]
                d['.'][k] = {'()':None}
            elif k.endswith('[]'):
                k = k[:-2]
                d['.'][k] = {'[]':None}
            elif v == []:
                d['.'][k] = None
            else:
                d['.'][k] = convert_tree(v)

        elif k[0]+k[-1] == '{}':
            return k

    return d


def merge_tree(tree, ref):
    # fills in {links}

    d = {}
    for k, v in tree.items():
        if v is None:
            d[k] = v
        elif isinstance(v, dict):
            d[k] = merge_tree(v, ref)
        elif v[0]+v[-1] == '{}':
            d[k] = ref[v[1:-1]]
        else:
            d[k] = v

    return d


def build_tree(filename):
    """Builds Telescope tree structure from YML file

    Reads YML file and parses it into a virtual object hierarchy

    Args:
        filename: A relative filepath to a valid YML file
            specifying a Telescope tree structure

    Returns:
        A dict corresponding to the abstract structure of the desired
        Telescope behavior. Values of this dict may be nested dicts.
        For example:

        {'()': None,
         '[]': {42: {'()':None}},
         '.':  {'bbb1':None,
                'bbb2':{'()':None}}}
    """

    # read file line-by-line, stripping whitespace from right
    # and ignoring blank lines
    with open(filename, 'r') as file:
        data = [line.rstrip() for line in file if line.rstrip() != '']

    # build a list of (line_indent, stripped_line) tuples for each line
    data = [(len(line)-len(line.lstrip()), line.lstrip()) for line in data]

    head = data[0][1]

    d = {}
    for k, v in foldr.from_list(data, simple=True):
        d[k] = v

    for k, v in d.items():
        d[k] = convert_tree(v)
    d = merge_tree(d, d)
    return d[head]

class Telescope(object):
    def __init__(self, d, callback, path=[]):
        if isinstance(d, str):
            self.d = build_tree(d)
        else:
            self.d = d

        self.callback = callback
        self.path = path

    def __getattr__(self, k):
        if not isinstance(self.d, dict):
            raise Exception('something')
        if '.' not in self.d.keys():
            raise Exception('something2')
        if k not in self.d['.'].keys():
            raise AttributeError(k)

        new_path = self.path+[Node(type='attr',
                                   val=k,
                                   args=None,
                                   kwargs=None)]
        if self.d['.'][k] is None:
            return self.callback(new_path)
        # else:
        return Telescope(self.d['.'][k],
                         self.callback,
                         new_path)

    def __getitem__(self, k):
        if '[]' not in self.d.keys():
            raise TypeError('object is not callable')

        try:
            temp_val = self.path.pop().val
        except:
            temp_val = None
        new_path = self.path+[Node(type='[]',
                                   val=temp_val,
                                   args=k,
                                   kwargs=None)]

        if self.d['[]'] == None:
            return self.callback(new_path)
        # else:
        return Telescope(self.d['[]'],
                         self.callback,
                         new_path)

    def __call__(self, *args, **kwargs):
        if '()' not in self.d.keys():
            raise TypeError('object is not callable')

        try:
            temp_val = self.path.pop().val
        except:
            temp_val = None

        new_path = self.path+[Node(type='()',
                                   val=temp_val,
                                   args=args,
                                   kwargs=kwargs)]

        if self.d['()'] == None:
            return self.callback(new_path)
        # else:
        return Telescope(self.d['()'],
                         self.callback,
                         new_path)
