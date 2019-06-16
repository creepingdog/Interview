import collections
import sys
import io


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

    def get_root(self):
        return self.__root
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
        root = self.get_root()

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

    @staticmethod
    def _is_same_tree(n1, n2):
        if not n1 and not n2:
            return True
        elif n1 and n2:
            return n1.get_data() == n2.get_data() and \
                   BiTree._is_same_tree(n1.get_left(), n2.get_left()) and \
                   BiTree._is_same_tree(n1.get_right(), n2.get_right())
        else:
            return False
        #
    #

    def __eq__(self, other):
        return BiTree._is_same_tree(self.get_root(), other.get_root())
    #

    def breadth_traversal(self, out=sys.stdout):
        stack = [(self.get_root(), 0)]

        while stack:
            (node, level) = stack.pop(0)
            out.write('{}({}) -> '.format(node.get_data(), level))

            left = node.get_left()
            if left:
                stack.append((left, level+1))
            #
            right = node.get_right()
            if right:
                stack.append((right, level + 1))
            #
        #
        out.write('[END]')
    #

    @staticmethod
    def _deep_traversal(node, parent_node=None, out=sys.stdout):
        if not node:
            return
        #
        out.write('{}({}) -> '.format(node.get_data(), parent_node.get_data() if parent_node else 'ROOT'))
        BiTree._deep_traversal(node.get_left(), parent_node=node, out=out)
        BiTree._deep_traversal(node.get_right(), parent_node=node, out=out)
    #

    def deep_traversal(self, out=sys.stdout):
        self._deep_traversal(self.get_root(), out=out)
        out.write('[END]')
    #
#