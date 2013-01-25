#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

A pure Python library for reading the width and height of PNG images.

See README.txt for details.
"""

import logging
import struct

import PNGFile
import GIFFile


def dimensions():
    import argparse

    # populate and parse command line options
    desc = 'Read the width and height of images.'
    desc += '\nhttp://github.com/philadams/dimensions'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('filenames', nargs='+',
            help='source image(s)')
    args = parser.parse_args()

    # logging config
    log_level = logging.WARNING  # default
    if args.verbose == 1:
        log_level = logging.INFO
    elif args.verbose >= 2:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)

    for filename in args.filenames:
        with open(filename, 'rb') as fp:

            if fp.read(len(PNGFile.SIGNATURE)) == PNGFile.SIGNATURE:
                fp.seek(0)
                img = PNGFile.PNGFile(fp)
            elif fp.read(len(GIFFile.SIGNATURE[0])) not in GIFFile.SIGNATURE:
                fp.seek(0)
                img = GIFFile.GIFFile(fp)
            else:
                raise NotImplementedError

            x, y = img.size
            print('%s\n  width: %d\n  height: %d' % (filename, x, y))

if '__main__' == __name__:
    dimensions()
