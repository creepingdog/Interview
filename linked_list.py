import collections

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    #
    def set_next(self, node):
        self.next = node
    #

    def __repr__(self):
        return str(self.value)
    #
#

class LinkedList(object):
    def __init__(self, head=None):
        self.head = None
        if isinstance(head, collections.Iterable):
            self.build(head)
        else:
            self.set_head(head)
        #
    #

    def set_head(self, head):
        self.head = head
    #

    def build(self, iterable):
        curr = None
        for i in iterable:
            node = Node(i)
            if self.head is None:
                self.head = node
                curr = self.head
            #
            if curr is None:
                curr = self.head
            else:
                curr.next = node
                curr = node
            #
        #
    #

    def __repr__(self):
        node = self.head
        desc = ''
        while node:
            desc = desc + str(node.value) + ' -> '
            node = node.next
        #
        desc = desc + '[END]'
        return desc
    #
#

def reverse_1(ll):
    pn = None
    cn = ll.head
    nn = None
    if cn is None:
        return ll
    #
    while cn:
        nn = cn.next
        cn.next = pn
        pn = cn
        cn = nn
    #
    ll.head = pn
    return ll
#


if __name__ == '__main__':
    a = range(9)
    ll = LinkedList(a)
    print(ll)

    reverse_1(ll)
    print(ll)
#