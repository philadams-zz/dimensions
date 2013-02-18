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


def get_dimensions(filenames):
    """given a sequence of filenames, compute dimensions
    return sequence of tuples (x, y, content_type, filename)"""

    dims = []
    for filename in filenames:
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
            dims.append((x, y, img.content_type, filename))
    return dims


def dimensions(filenames):
    """given a filename or list of filenames,
    return a tuple or sequence of tuples (x, y, filename)"""

    single = type(filenames) is str
    if single:
        filenames = [filenames]
    dims = get_dimensions(filenames)
    if single:
        dims = dims[0]
    return dims


def cli():
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

    dims = get_dimensions(args.filenames)
    for x, y, content_type, filename in dims:
        print('%s\n  width: %d\n  height: %d\n  content_type: %s' % (filename, x, y, content_type))

if '__main__' == __name__:
    dimensions()
