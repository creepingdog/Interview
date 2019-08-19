class A(object):
    def __new__(cls, *args, **kwargs):
        print('[A::__new__] This is the ID of cls {}: {}({})'.format(cls, id(cls), hex(id(cls))))
        clz = super().__new__(cls)
        print('[A::__new__] This is the return of __new__ method: {}'.format(clz))
        return clz
    #

    def __init__(self):
        print('[A::__init__] This is self in __init__ method: {}'.format(self))
    #
#


if __name__ == '__main__':
    print('This is the ID of Class A: {}({})'.format(id(A), hex(id(A))))
    a = A()
    print('This is the ID of an instance of Class A: {}({})'.format(id(a), hex(id(a))))
