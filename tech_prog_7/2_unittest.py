import unittest
from main import merge_sort


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.merge_sort = merge_sort()
