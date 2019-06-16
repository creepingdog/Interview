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

    def test_add(self):
        linked_list = ll.LinkedList([-3.4, 'check', 78, None])
        linked_list.add('new')
        self.assertEqual(str(linked_list), '-3.4 -> check -> 78 -> None -> new -> [END]')
    #

    def test_reverse(self):
        linked_list = ll.LinkedList([4, 9, -1, 7, 2])
        linked_list.reverse()
        self.assertEqual(str(linked_list), '2 -> 7 -> -1 -> 9 -> 4 -> [END]')
    #

    def test_swap_pairs(self):
        linked_list = ll.LinkedList(('This', 'is', 'a', 'linked', 'list'))
        linked_list.swap_pairs()
        self.assertEqual(str(linked_list), 'is -> This -> linked -> a -> list -> [END]')

        linked_list = ll.LinkedList([-5, 9.4])
        linked_list.swap_pairs()
        self.assertEqual(str(linked_list), '9.4 -> -5 -> [END]')

        linked_list = ll.LinkedList([4, 9, -1, 7, 2, 10.5])
        linked_list.swap_pairs()
        self.assertEqual(str(linked_list), '9 -> 4 -> 7 -> -1 -> 10.5 -> 2 -> [END]')
    #


if __name__ == '__main__':
    unittest.main()
#
