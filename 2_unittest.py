import unittest
from main import Root


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.root = Root()

    def test_1(self):
        self.assertEqual(self.root.get_root(25), 5)

    def test_2(self):
        self.assertIs(type(self.root.get_root(12)), int)

    def test_3(self):
        self.assertIs(type(self.root.get_root(12.5)), int)


if __name__ == '__main__':
    unittest.main()
