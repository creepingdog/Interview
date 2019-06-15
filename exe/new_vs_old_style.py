from sys import version_info


class Old:
    pass
#


class New(object):
    pass
#


def show_type_diff():
    old_instance = Old()
    new_instance = New()

    python_version = '{}.{}'.format(version_info.major, version_info.minor)
    print('Python version is {}. '.format(python_version), end='')

    if version_info.major == 3:
        # In Python 3, all classes definitions are new-style
        print('Old-style classes are removed.')
        print('new_instance.__class__   : {}'.format(new_instance.__class__))
        print('type(new_instance)       : {}'.format(type(new_instance)))
    else:
        # In Python 2, there are differences between class definitions
        print('For old-style class, type() function returns: {}'.format(type(old_instance)))
        print('For new-style class, type() function returns: {}'.format(type(new_instance)))
    #
#


if __name__ == '__main__':
    show_type_diff()
#
