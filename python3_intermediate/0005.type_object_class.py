

if __name__ == '__main__':
    print('\n"object" instantiated by whom?')
    print(type(object))  # <class 'type'>

    print('\n"object" inherited from which class')
    print(object.__bases__)  # ()

    print('\n"type" instantiated by whom')
    print(type(type))  # <class 'type'>

    print('\n"type" inherited from which class')
    print(type.__bases__)  # (<class 'object'>,)

    # define a variable
    value = 100

    print('\nAn int variable is instantiated by whom?')
    print(type(value))  # <class 'int'>

    print('\n"int" instantiated by whom')
    print(type(int))  # <class 'type'>

    print('\n"int" inherited from which class?')
    print(int.__bases__)  # (<class 'object'>,)
