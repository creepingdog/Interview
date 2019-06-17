import unittest
import lib.struct.binary_tree as bt
import io


class TestLinkedList(unittest.TestCase):
    def test_build_on_list(self):
        btree = bt.BiTree([4, [9, [2, [5, None, None], [3, None, None]], ['test', None, None]],
                        [8, [100.3, None, None], [-5.0, None, None]]])
        btree.display()
    #

    def test_eq(self):
        t1 = bt.BiTree([4, [9, [2, [5, None, None], [3, None, None]], ['test', None, None]],
                        [8, [100.3, None, None], [-5.0, None, None]]])
        t2 = bt.BiTree([4, [9, [2, [5, None, None], [3, None, None]], ['test', None, None]],
                        [8, [100.3, None, None], [-5.0, None, None]]])
        self.assertEqual(t1, t2)

        t3 = bt.BiTree([4, [9, [2, [5, None, None], [3, None, None]], ['test', None, None]],
                        [8, [100.3, None, None], None]])
        self.assertNotEqual(t1, t3)
    #

    def test_breath_traversal(self):
        out = io.StringIO()
        btree = bt.BiTree([4, [9, [2, [5, None, None], [3, None, None]], ['test', None, None]],
                        [8, [100.3, None, None], [-5.0, None, None]]])
        btree.breadth_traversal(out=out)
        ret = out.getvalue()
        out.close()
        self.assertEqual(ret, '4(0) -> 9(1) -> 8(1) -> 2(2) -> test(2) -> 100.3(2) -> -5.0(2) -> 5(3) -> 3(3) -> [END]')
    #

    def test_preorder_traversal(self):
        out = io.StringIO()
        btree = bt.BiTree([4, [9, [2, [5, None, None], [3, None, None]], ['test', None, None]],
                        [8, [100.3, None, None], [-5.0, None, None]]])
        btree.preorder_traversal(out=out)
        ret = out.getvalue()
        out.close()
        self.assertEqual(ret, '4(ROOT) -> 9(4) -> 2(9) -> 5(2) -> 3(2) -> test(9) -> 8(4) -> 100.3(8) -> -5.0(8) -> [END]')
    #

    def test_inorder_traversal(self):
        out = io.StringIO()
        btree = bt.BiTree([4, [9, [2, [5, None, None], [3, None, None]], ['test', None, None]],
                        [8, [100.3, None, None], [-5.0, None, None]]])
        btree.inorder_traversal(out=out)
        ret = out.getvalue()
        out.close()
        self.assertEqual(ret, '5(2) -> 2(9) -> 3(2) -> 9(4) -> test(9) -> 4(ROOT) -> 100.3(8) -> 8(4) -> -5.0(8) -> [END]')
    #

    def test_postorder_traversal(self):
        out = io.StringIO()
        btree = bt.BiTree([4, [9, [2, [5, None, None], [3, None, None]], ['test', None, None]],
                        [8, [100.3, None, None], [-5.0, None, None]]])
        btree.postorder_traversal(out=out)
        ret = out.getvalue()
        out.close()
        self.assertEqual(ret, '-5.0(8) -> 100.3(8) -> 8(4) -> test(9) -> 3(2) -> 5(2) -> 2(9) -> 9(4) -> 4(ROOT) -> [END]')
    #
#


if __name__ == '__main__':
    unittest.main()
#
