import os
import Image
import unittest
import imgdupcheck

TESTDIR = 'test'


class ImgdupcheckTests(unittest.TestCase):

    def setUp(self):
        self.base = Image.open(os.path.join(TESTDIR, 'py-orig.png')).getdata()
        self.good = Image.open(os.path.join(TESTDIR, 'py-copy.png')).getdata()
        self.bad = Image.open(os.path.join(TESTDIR, 'py-2.png')).getdata()

    def test_base_and_good_same(self):
        self.assertTrue(imgdupcheck.is_the_same(self.base, self.good))

    def test_base_and_bad_diff(self):
        self.assertFalse(imgdupcheck.is_the_same(self.base, self.bad))

    def test_good_and_bad_diff(self):
        self.assertFalse(imgdupcheck.is_the_same(self.good, self.bad))
