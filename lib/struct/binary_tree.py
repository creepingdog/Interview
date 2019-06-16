import collections


class Node(object):
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None
    #

    def set_data(self, data):
        self.__data = data
    #

    def set_left(self, left_node):
        self.__left = left_node
    #

    def set_right(self, right_node):
        self.__right = right_node
    #

    def get_data(self):
        return self.__data
    #

    def get_left(self):
        return self.__left
    #

    def get_right(self):
        return self.__right
    #

    def __repr__(self):
        return '[Data] {}, [Left] {}, [Right] {}'.format(self.__data, self.__left, self.__right)
    #

    def display(self, is_left, indent):
        # print()
        right = self.get_right()
        if right:
            right.display(False, '{}{}'.format(indent, ' |  ' if is_left else '    '))
        #
        print(indent, end='')
        if is_left:
            print(' \\', end='')
        else:
            print(' /', end='')
        #
        print('-- ', end='')
        print(self.__data)

        left = self.get_left()
        if left:
            left.display(True, '{}{}'.format(indent,  '    ' if is_left else ' |  '))
        #
    #
#


class BiTree(object):
    def __init__(self, root=None):
        self.__root = None
        if isinstance(root, collections.Iterable):
            root = self.build(root)
            self.set_root(root)
        else:
            self.set_root(root)
        #
    #

    def set_root(self, root):
        self.__root = root
    #

    def build(self, iterable):
        if iterable is None:
            return None
        #
        if len(iterable) != 3:
            raise Exception('There should be 3 items in the iterable')
        #
        root = Node(iterable[0])
        root.set_left(self.build(iterable[1]))
        root.set_right(self.build(iterable[2]))
        return root
    #

    def display(self):
        print()
        root = self.__root

        if not root:
            return
        #
        right = root.get_right()
        if right:
            right.display(False, '')
        #
        print(root.get_data())
        left = root.get_left()
        if left:
            left.display(True, '')
        #
    #

    # def __repr__(self, prefix, is_tail):
    #     layout =
#