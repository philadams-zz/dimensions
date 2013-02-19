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
      content_type: image/png

Wildcards also work (escape \* in markdown for PyPi RST...):

    > dimensions src/\*.png
    src/sample.png
      width: 405
      height: 239
      content_type: image/png
    src/sample2.png
      width: 473
      height: 469
      content_type: image/png

As always, full details are available via `dimensions -h`.

In Python code, simply call `dimensions.dimensions`. If you provide a
sequence of filenames, you get back a sequence of tuples; if you provide
just a single filename, you get back a single tuple.

    import dimensions
    dims = dimensions.dimensions('./src/sample.png')
    # (405, 239, 'image/png', './src/sample.png')

future
------

- test for in-python codes
- release newer version to PyPi
