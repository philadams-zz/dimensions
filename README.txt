dimensions
==========

A pure Python library for reading the width, height, and rotation of PNG
images.

usage
-----

    > dimensions src/sample.png
    src/sample.png
      width: 405px
      height: 239px

As always, full details are available via `dimensions -h`.

future
------

- PNG organize as chunkstream, or at least class PNGImage as list of
  Chunks. perhaps organize chunks as functions instead? have to figure
  out how to call subclasses of Chunk based on chunk\_type string.
- PNG width/height
- organize into ./dimensions/ dir by module
- PNG rotation?
- pip registration (dimensions)
- allow for lists of input files a la `dimensions *.png`
- JPEG, GIF
