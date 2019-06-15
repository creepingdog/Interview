class ObjectCreator(object):
    pass
#


def echo(o):
    print(o)
#


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        #
        return Foo     # return class, not instance
    else:
        class Bar(object):
            pass
        #
        return Bar
    #
#


def echo_shiny(self):
    print(self.shiny)
#


if __name__ == '__main__':
    # Class could be passed in functions as arguments
    print('Class could be passed in functions as arguments.')
    print('echo(ObjectCreator): ', end='')
    echo(ObjectCreator)
    print()

    # Class attribute
    print('Before adding "new_attribute": hasattr(ObjectCreator, "new_attribute") = {}'.format(
        hasattr(ObjectCreator, 'new_attribute')))
    ObjectCreator.new_attribute = 'foo'
    print(
        'After adding "new_attribute": hasattr(ObjectCreator, "new_attribute") = {}, ObjectCreator.new_attribute = {}'.format(
            hasattr(ObjectCreator, 'new_attribute'), ObjectCreator.new_attribute))
    print()

    # Create class dynamically
    MyClass = choose_class('foo')
    print('Dynamically create a class. MyClass: ', end='')
    print(MyClass)
    print('And it can be used like usual class. MyClass(): ', end='')
    print(MyClass())
    print()

    # Even more dynamically
    MyShinyClass = type('MyShinyClass', (object,), {'shiny': True, 'echo_shiny':echo_shiny})
    print('Even more dynamically. MyShinyClass: ', end='')
    print(MyShinyClass)
    print('And instance. MyShinyClass(): ', end='')
    sc = MyShinyClass()
    print(sc)
    print('Member variable. MyShinyClass().shiny: ', end='')
    print(sc.shiny)
    print('Member function. MyShinyClass().echo_shiny(): ', end='')
    sc.echo_shiny()
    print()

    # check type
    age = 35
    print('age.__class__: ', end='')
    print(age.__class__)

    name = 'bob'
    print('name.__class__: ', end='')
    print(name.__class__)

    def foo(): pass
    print('function: foo.__class__: ', end='')
    print(foo.__class__)

    print('class: ObjectCreator.__class__: ', end='')
    print(ObjectCreator.__class__)

    print('instance: ObjectCreator().__class__: ', end='')
    print(ObjectCreator().__class__)

    print()

    print('age.__class__.__class__: ', end='')
    print(age.__class__.__class__)

    print('name.__class__.__class__: ', end='')
    print(name.__class__.__class__)

    print('foo.__class__.__class__: ', end='')
    print(foo.__class__.__class__)

    print('ObjectCreator.__class__.__class__: ', end='')
    print(ObjectCreator.__class__.__class__)

    print('ObjectCreator().__class__.__class__: ', end='')
    print(ObjectCreator().__class__.__class__)

    print()

#