
class UpperAttrMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        uppercase_attrs = {}
        for name, val in attrs.items():
            if not name.startswith('__'):
                uppercase_attrs[name.upper()] = val
            else:
                uppercase_attrs[name] = val
            #
        #
        return type.__new__(mcs, name, bases, uppercase_attrs)
    #
#


class Foo(object, metaclass=UpperAttrMetaclass):  # global __metaclass__ won't work with "object" though
    bar = 'bip'
#


if __name__ == '__main__':
    print('Class variables are modified by __metaclass__: ')
    print('hasattr(Foo, "bar") = ', end='')
    print(hasattr(Foo, 'bar'))
    print('hasattr(Foo, "BAR") = ', end='')
    print(hasattr(Foo, 'BAR'))

    print('Foo().BAR: ', end='')
    f = Foo()
    print(f.BAR)
#
