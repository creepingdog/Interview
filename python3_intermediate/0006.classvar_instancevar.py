class A(object):
    class_var = 3.14

    def __init__(self):
        self.instance_var = 6.28
    #
#


if __name__ == '__main__':
    print('\nClass variable can be accessed thru class itself or an instance. However instance variable can be only accessed thru an instance:')
    print(A.class_var)
    print(A().class_var)
    print(A().instance_var)

    print('\nClass variable modified thru an instance will not affected the class or other instances:')
    a = A()
    a.class_var = -3.14
    print(a.class_var)
    print(A.class_var)
    print(A().class_var)

    print('\nClass variable modified thru class itself will affect other instances:')
    A.class_var = -6.28
    print(A.class_var)
    print(A().class_var)
#