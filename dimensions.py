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
    """A PNG Chunk.
    Parses one chunk from a PNG stream (file reader interface) into 4 fields:
        - a length (4 byte unsigned int)
        - a chunk type (4 bytes, chars)
        - data (length bytes, various)
        - crc (4 bytes)
    Chunk does not close or otherwise mess with the stream. Chunk should be
    subclassed to handle parsing of the data field for specific chunks, e.g.
    IHDR or IDAT.
    Note: all integer values in PNG streams are big endian"""

    _length = struct.Struct('>L')
    _chunk_type = struct.Struct('cccc')

    def __init__(self, fp):
        self.fp = fp
        raw = fp.read(Chunk._length.size)
        self.length = int(Chunk._length.unpack(raw)[0])
        raw = fp.read(Chunk._chunk_type.size)
        self.chunk_type = ''.join(Chunk._chunk_type.unpack(raw))
        self.data_raw = fp.read(self.length)
        self.crc_raw = fp.read(4)


class IDHRChunk(Chunk):
    """A PNG IDHR chunk.
    Parses the chunk's data field according to:
    TODO"""
    pass


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

    # read whole file into list of bytes
    #data = []
    #with open(args.filename, 'rb') as f:
    #    while True:
    #        block = f.read(1)
    #        if not block:
    #            break
    #        data.append(block)
    #print map(None, data[:8])
    #print map(None, data[8:12])
    #print map(ord, data[8:12])
    #print struct.unpack('>L', ''.join(data[8:12]))
    #print map(None, data[12:16])

    # parse PNG:
    #   first, the magic signature (8 bytes)
    #   then a series of chunks
    with open(args.filename, 'rb') as fp:
        magic = fp.read(8)
        if magic != SIGNATURE:
            print('%s is not PNG signature' % magic)
            exit()
        ihdr = Chunk(fp)
        print 'reading chunks correctly:', ihdr.chunk_type, ihdr.length


if '__main__' == __name__:
    main()
