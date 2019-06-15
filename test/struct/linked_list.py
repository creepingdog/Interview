import unittest
import lib.struct.linked_list as ll


class TestLinkedList(unittest.TestCase):

    def test_build_on_list(self):
        linked_list = ll.LinkedList([4, 9, -1, 7, 2])
        self.assertEqual(str(linked_list), '4 -> 9 -> -1 -> 7 -> 2 -> [END]')
    #

    def test_build_on_tuple(self):
        linked_list = ll.LinkedList(('This', 'is', 'a', 'linked', 'list'))
        self.assertEqual(str(linked_list), 'This -> is -> a -> linked -> list -> [END]')
    #

    def test_reverse(self):
        linked_list = ll.LinkedList([4, 9, -1, 7, 2])
        linked_list.reverse()
        self.assertEqual(str(linked_list), '2 -> 7 -> -1 -> 9 -> 4 -> [END]')
    #


if __name__ == '__main__':
    unittest.main()
#
