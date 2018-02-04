import types
import copy

#struct = {'Chart':{'spine':{'left':{'visible':'()'},
#                            'right':{'visible':'()'}}}}
'''
def factory(lst,f,callback):
    class Layer(object):
        def __init__(self,lst,f,callback):
            self.lst = lst
            self.f = f
            self.callback = callback

        def __getattr__(self,k):
            if type(self.lst) != dict:
                raise Exception('something')

            if k in self.lst.keys():
                return self.f(self.lst[k],
                              self.f,
                              self.callback)
            else:
                raise Exception('something else')

        def handle(self,route,args,kwargs):
            pass

        def __call__(self,*args,**kwargs):
            return self.callback(args,kwargs)

    class Wrapper(object):
        base = Layer(lst,f,callback)

        def __init__(self):
            self._base = copy.deepcopy(base)

        def __getattr__(self,k):
            if type(self.lst) != dict:
                raise Exception('something')

            if k in self.lst.keys():
                return self.f(self.lst[k],
                              self.f,
                              self.callback)
            else:
                raise Exception('something else')

    return Wrapper

def go_bananas(s):
    return factory(s,factory,print)



struct = {'spine':{'left':{'visible':'()'},
                   'right':{'visible':'()'}}}

Prototype = go_bananas(struct)

class Example(Prototype):
    def __init__(self):
        pass

a = Example()
a.spine
'''
'''
class Chart(Prototype):
    def handle(self,route,args,kwargs):
        print(route,args,kwargs)
        return 'hello there'

chart = go_bananas(Chart(),struct)
chart.spine
'''
'''
Prototype = factory(struct,)

a = factory(struct,factory,print)
a.spine.left.visible('hello')
'''






'''
class Dog:
    def bark(self):
        print 'Woof!'

def herd(self, sheep):
    self.run()
    self.bark()
    self.run()

border_collie = Dog()
border_collie.herd  = types.MethodType(herd, border_collie)
'''




class Telescope(object):
    pass


struct = {'spine':{'left':{'visible':'()'},
                   'right':{'visible':'()'}}}

class Example(object):
    def __init__(self):
        self._telescope = Telescope(struct,self.handle)

    def handle(self,*args,**kwargs):
        print(args,kwargs)
