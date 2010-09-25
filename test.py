import os
import Image
import unittest
import imgdupcheck

TESTDIR = 'test'


class ImgdupcheckTests(unittest.TestCase):

    def setUp(self):
        self.orig = Image.open(os.path.join(TESTDIR, 'dups', 'py-orig.png'))
        self.copy = Image.open(os.path.join(TESTDIR, 'dups', 'py-copy.png'))
        self.copy2 = Image.open(os.path.join(TESTDIR, 'dups', 'py-copy-2.png'))
        self.other = Image.open(os.path.join(TESTDIR, 'dups', 'py-2.png'))
        self.othercopy = Image.open(os.path.join(TESTDIR, 'dups', 'py-2-copy.png'))

    def test_orig_and_copy_same(self):
        self.assertTrue(imgdupcheck.is_same_image(self.orig, self.copy))

    def test_orig_and_other_diff(self):
        self.assertFalse(imgdupcheck.is_same_image(self.orig, self.other))

    def test_copy_and_other_diff(self):
        self.assertFalse(imgdupcheck.is_same_image(self.copy, self.other))

    def test_check_dir_without_dups(self):
        nodups = imgdupcheck.check_images(os.path.join(TESTDIR, 'nodups'))
        self.assertTrue(len(nodups) == 0)

    def test_check_dir_with_dups(self):
        dups = imgdupcheck.check_images(os.path.join(TESTDIR, 'dups'))
        self.assertTrue(len(dups) == 2)
        dupset_orig = set(dups[0])
        self.assertTrue(len(dupset_orig) == 3)
        self.assertEqual(dupset_orig, set([self.orig.filename, 
                                           self.copy.filename,
                                           self.copy2.filename
                                           ]))
        dupset_other = set(dups[1])
        self.assertTrue(len(dupset_other) == 2)
        self.assertEqual(dupset_other, set([self.other.filename,
                                            self.othercopy.filename
                                            ]))

