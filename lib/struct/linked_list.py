import collections


class Node(object):
    def __init__(self, data):
        self.__data = data
        self.__next = None
    #

    def set_next(self, node):
        self.__next = node
    #

    def get_data(self):
        return self.__data
    #

    def get_next(self):
        return self.__next
    #

    def __repr__(self):
        return '[Data] {}, [Next]: {}'.format(self.__data, self.__next)
    #
#


class LinkedList(object):
    def __init__(self, head=None):
        self.__head = None
        if isinstance(head, collections.Iterable):
            self.build(head)
        else:
            self.set_head(head)
        #
    #

    def set_head(self, head):
        self.__head = head
    #

    def build(self, iterable):
        curr = None
        for i in iterable:
            node = Node(i)
            if self.__head is None:
                self.__head = node
                curr = self.__head
            #
            if curr is None:
                curr = self.__head
            else:
                curr.set_next(node)
                curr = node
            #
        #
    #

    def add(self, data):
        node = Node(data)
        head = self.__head
        if head is None:
            self.set_head(node)
        else:
            curr = head
            while curr.get_next():
                curr = curr.get_next()
            #
            curr.set_next(node)
        #
    #

    def reverse(self):
        prev_node = None
        curr_node = self.__head
        next_node = None
        if curr_node is None:
            return
        #
        while curr_node:
            next_node = curr_node.get_next()
            curr_node.set_next(prev_node)
            prev_node = curr_node
            curr_node = next_node
        #
        self.set_head(prev_node)
    #

    def __repr__(self):
        node = self.__head
        desc = ''
        while node:
            data = node.get_data()
            desc = '{}{} -> '.format(desc, str(data))
            node = node.get_next()
        #
        desc = desc + '[END]'
        return desc
    #
#


# def reverse_1(ll):
#     pn = None
#     cn = ll.head
#     nn = None
#     if cn is None:
#         return ll
#     #
#     while cn:
#         nn = cn.next
#         cn.next = pn
#         pn = cn
#         cn = nn
#     #
#     ll.head = pn
#     return ll
# #
