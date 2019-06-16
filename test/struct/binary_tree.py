import unittest
import lib.struct.binary_tree as bt


class TestLinkedList(unittest.TestCase):
    def test_build_on_list(self):
        btree = bt.BiTree([4, [9, [2, [5, None, None], [3, None, None]], ['test', None, None]], [8, [100.3, None, None], [-5.0, None, None]]])
        btree.display()
    #
#


if __name__ == '__main__':
    unittest.main()
#
#

