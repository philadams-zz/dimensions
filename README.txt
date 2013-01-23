dimensions
==========

A pure Python library for reading the width and height of images.

usage
-----

For a single image:

    > dimensions src/sample.png
    src/sample.png (405, 239)

Wildcards also work (the escape '\' is only for PyPi RST...):

    > dimensions src/\*.png
    src/sample.png (405, 239)
    src/sample2.png (473, 469)

As always, full details are available via `dimensions -h`.

future
------

- GIF
- organize into ./dimensions/ dir by module
- confirm working as importable module
- tests
- JPEG
