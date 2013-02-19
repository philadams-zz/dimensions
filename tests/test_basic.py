# -*- coding: utf-8 -*-

from context import dimensions

import unittest


class GIFTest(unittest.TestCase):

    def setUp(self):
        self.fname = '../sample/sample.gif'
        self.content_type = 'image/gif'
        self.dims = dimensions.dimensions(self.fname)

    def test_x(self):
        self.assertEqual(self.dims[0], 250)

    def test_y(self):
        self.assertEqual(self.dims[1], 297)

    def test_content_type(self):
        self.assertEqual(self.dims[2], self.content_type)

    def test_fname(self):
        self.assertEqual(self.dims[3], self.fname)


class PNGTest(unittest.TestCase):

    def setUp(self):
        self.fname = '../sample/sample.png'
        self.content_type = 'image/png'
        self.dims = dimensions.dimensions(self.fname)

    def test_x(self):
        self.assertEqual(self.dims[0], 405)

    def test_y(self):
        self.assertEqual(self.dims[1], 239)

    def test_content_type(self):
        self.assertEqual(self.dims[2], self.content_type)

    def test_fname(self):
        self.assertEqual(self.dims[3], self.fname)


class JPEGTest(unittest.TestCase):

    def setUp(self):
        self.fname = '../sample/sample.jpg'
        self.content_type = 'image/jpeg'
        self.dims = dimensions.dimensions(self.fname)

    def test_x(self):
        self.assertEqual(self.dims[0], 313)

    def test_y(self):
        self.assertEqual(self.dims[1], 234)

    def test_content_type(self):
        self.assertEqual(self.dims[2], self.content_type)

    def test_fname(self):
        self.assertEqual(self.dims[3], self.fname)


class OtherTests(unittest.TestCase):

    def test_handles_single_file(self):
        fname = '../sample/sample.png'
        dims = dimensions.dimensions(fname)
        self.assertTrue(type(dims) is tuple)

    def test_handles_multiple_files(self):
        fnames = ('../sample/sample.gif', '../sample/sample.png')
        dims = dimensions.dimensions(fnames)
        self.assertTrue(type(dims) is list)


if __name__ == '__main__':
    unittest.main()
