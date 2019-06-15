class MyClass(object):
    def f(self):
        print('f()')
    #
#


def monkey_f(self):
    print('monkey_f()')
#


if __name__ == '__main__':
    x1 = MyClass()
    print('===== Before monkey patching =====')
    print('x1.f() => ', end='')
    x1.f()
    print()

    MyClass.f = monkey_f
    x2 = MyClass()
    print('===== After monkey patching =====')
    print('x2.f() => ', end='')
    x2.f()
    print()

    # This changes as well! Very dangerous #
    print('===== Monkey patching changes x1 as well! Very dangerous! =====')
    print('x1.f() => ', end='')
    x1.f()
    print()
#
