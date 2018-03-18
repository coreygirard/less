class FoldrNode(object):
    def __init__(self, depth, code):
        '''
        >>> node = FoldrNode(0,'aaa')
        >>> node.add(FoldrNode(1,'bbb'))
        >>> node.add(FoldrNode(2,'ccc'))

        >>> node.depth
        0

        >>> node.code
        'aaa'

        >>> node.parent
        '''

        self.depth = depth
        self.code = code
        self.parent = None
        self.children = []

    def add(self, child):
        '''
        >>> node1 = FoldrNode(0,'aaa')
        >>> node2 = FoldrNode(1,'bbb')
        >>> node1.add(node2)

        >>> node1.children[0] == node2
        True
        >>> node2.parent == node1
        True
        '''

        child.parent = self
        self.children.append(child)


def simplify(head):
    '''
    >>> head = FoldrNode(0,'aaa')
    >>> head.add(FoldrNode(1,'bbb'))
    >>> head.add(FoldrNode(2,'ccc'))

    >>> simplify(head)
    ['aaa', [['bbb', []], ['ccc', []]]]
    '''

    resp = [head.code, []]
    for node in head.children:
        resp[1].append(simplify(node))
    return resp

def from_list(lines, simple=False):
    '''
    >>> data = [(0,'aaa'),
    ...         (1,'bbb'),
    ...         (2,'ccc'),
    ...         (1,'ddd'),
    ...         (2,'eee'),
    ...         (2,'fff')]
    >>> r = from_list(data,simple=True)
    >>> r == [['aaa',
    ...        [['bbb',
    ...          [['ccc', []]]],
    ...         ['ddd',
    ...          [['eee', []],
    ...           ['fff', []]]]]]]
    True
    '''

    root = FoldrNode(-4, '')
    ptr = root
    for depth, code in lines:
        line = FoldrNode(depth, code)

        if line.depth > ptr.depth:
            ptr.add(line)
            ptr = ptr.children[-1]
        elif line.depth == ptr.depth:
            ptr = ptr.parent
            ptr.add(line)
            ptr = ptr.children[-1]
        else:
            while line.depth < ptr.depth:
                ptr = ptr.parent
            ptr = ptr.parent
            ptr.add(line)
            ptr = ptr.children[-1]

    if simple:
        return [simplify(c) for c in root.children]
    # else:
    return [c for c in root.children]


def from_attribute(lines, attr, simple=False):
    data = []
    for line in lines:
        try:
            data.append((getattr(line, attr), line))
        except AttributeError:
            # TODO: anything
            pass

    return from_list(data, simple)

def from_method(lines, attr, simple=False):
    data = []
    for line in lines:
        try:
            data.append((getattr(line, attr)(), line))
        except AttributeError:
            # TODO: anything
            pass

    return from_list(data,simple)



def collapse_chars(s):
    during = [s.pop(0)]
    while s != []:
        if isinstance(during[-1], str) and isinstance(s[0], str):
            during[-1] += s.pop(0)
        else:
            during.append(s.pop(0))
    return during


# TODO: optimize
def lisp(line, char=None):
    if not char:
        start, finish = '(', ')'
    else:
        start, finish = char

    line = list(line)

    assert line.count(start) == line.count(finish)


    while start in line:
        last = None
        i = 0
        while True:
            if i >= len(line):
                break
            if line[i] == start:
                last = i
            if line[i] == finish:
                break
            i += 1

        if i >= len(line):
            break

        if last != None:
            before = line[:last]
            during = collapse_chars(line[last+1:i])

            after = line[i+1:]
            line = before+[during]+after

    return collapse_chars(line)
