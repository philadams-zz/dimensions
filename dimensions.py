#!/usr/bin/env python

"""
Phil Adams http://philadams.net

A pure Python library for reading the width, height, and rotation of PNG images.

See README.txt for details.
"""

import logging
import struct


SIGNATURE = '\211PNG\r\n\032\n'


class Chunk(object):
    """A PNG Chunk is composed of 4 fields:
        - a length (4 byte unsigned int)
        - a type (4 bytes, chars)
        - data (length bytes, various)
        - crc (4 bytes)
    Note: all integer values in PNG streams are big endian"""

    _length = struct.Struct('>L')
    _type = struct.Struct('cccc')
    _crc = 4
    _end_type = 'IEND'


class PNGFile(object):
    """A PNG Image"""

    def __init__(self, fp):
        self.fp = fp
        self.chunks = []
        self._load()
        self.header = self.chunks[0]['data']
        self.size = (self.header['width'], self.header['height'])

    def _load(self):

        # confirm PNG format
        magic = self.fp.read(len(SIGNATURE))
        if magic != SIGNATURE:
            # TODO: raise appropriate exception
            print('%s is not PNG signature' % magic)
            exit()

        # parse chunk stream
        l, t, c = Chunk._length, Chunk._type, Chunk._crc
        while True:

            # parse a chunk
            chunk = {}
            chunk['length'] = l.unpack(self.fp.read(l.size))[0]
            chunk['type'] = ''.join(t.unpack(self.fp.read(t.size)))
            parse_data = '%s_data' % chunk['type']
            if hasattr(self, parse_data):
                chunk['data'] = getattr(self, parse_data)()
            else:
                chunk['data'] = self.fp.read(chunk['length'])
            chunk['crc'] = self.fp.read(c)

            # store in chunks dict
            self.chunks.append(chunk)
            if chunk['type'] == Chunk._end_type:
                break
            # for now, we just need the IHDR chunk
            if chunk['type'] == 'IHDR':
                break

    def IHDR_data(self):
        dim = struct.Struct('>L')
        sbyte = struct.Struct('c')
        data = {}
        data['width'] = dim.unpack(self.fp.read(dim.size))[0]
        data['height'] = dim.unpack(self.fp.read(dim.size))[0]
        data['bit_depth'] = ord(sbyte.unpack(self.fp.read(sbyte.size))[0])
        data['color_type'] = ord(sbyte.unpack(self.fp.read(sbyte.size))[0])
        data['compression_method'] = ord(sbyte.unpack(self.fp.read(sbyte.size))[0])
        data['filter_method'] = ord(sbyte.unpack(self.fp.read(sbyte.size))[0])
        data['interlace_method'] = ord(sbyte.unpack(self.fp.read(sbyte.size))[0])
        return data


def main():
    import argparse

    # populate and parse command line options
    desc = 'Read the width, height, and rotation of images.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('filename', help='source image')
    args = parser.parse_args()

    # logging config
    log_level = logging.WARNING  # default
    if args.verbose == 1:
        log_level = logging.INFO
    elif args.verbose >= 2:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)

    with open(args.filename, 'rb') as fp:
        png = PNGFile(fp)
    x, y = png.size
    print('%s\n  width: %d\n  height: %d' % (args.filename, x, y))


if '__main__' == __name__:
    main()
