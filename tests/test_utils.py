# core modules
import unittest

# internal modules
import clana.utils


class UtilsTest(unittest.TestCase):
    def test_load_labels(self):
        clana.utils.load_labels("~/.clana/data/labels.csv", 10)
