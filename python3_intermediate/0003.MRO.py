class A(object):
    def say_hello(self):
        print('[A::say_hello] Hello!')
    #
#


class B(object): pass


class C(object): pass


class E(A, B): pass


class F(B, C):
    def say_hello(self):
        print('[F::say_hello] Hello!')
    #
#


class G(E, F): pass



if __name__ == '__main__':
    print('The following shows C3 is not DFS:')
    print('E.mro(): {}'.format(E.mro()))

    print('\nThe following shows C3 is not BFS neither:')
    print('G.mro(): {}'.format(G.mro()))
    print('G.__mro__: {}'.format(G.__mro__))

    print('\nUnlike .mro() or .__mro__, __bases__ only shows direct parent classes:')
    print('G.__bases__: {}'.format(G.__bases__))
    print('A.__bases__: {}'.format(A.__bases__))

    print('\nInheritance uses MRO C3 to get the first hit:')
    g = G()
    g.say_hello()
#