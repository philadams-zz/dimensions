dimensions
==========

A pure Python library for reading the width and height of PNG images.

usage
-----

For a single image:

    > dimensions src/sample.png
    src/sample.png
      width: 405
      height: 239

Wildcards also work:

    > dimensions src/*.png
    src/sample.png
      width: 405
      height: 239
    src/sample2.png
      width: 473
      height: 469

As always, full details are available via `dimensions -h`.

future
------

- pip registration (dimensions)
- GIF
- organize into ./dimensions/ dir by module
- confirm working as importable module
- tests
- JPEG
