dimensions
==========

A pure Python library for reading the width and height of images.

installation
------------

`pip install dimensions`

Done.

usage
-----

For a single image:

    > dimensions src/sample.png
    src/sample.png
      width: 405
      height: 239

Wildcards also work (escape \* in markdown for PyPi RST...):

    > dimensions src/\*.png
    src/sample.png
      width: 405
      height: 239
    src/sample2.png
      width: 473
      height: 469

As always, full details are available via `dimensions -h`.

future
------

- better entry interface; confirm working as importable module
- tests
- JPEG
