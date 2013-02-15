#!/usr/bin/env roundup

describe "dimensions: Python lib to read the height and with of image files"

before() {
    cd ../bin
}

after() {
    cd ../tests
}

dimensions="./dimensions"

it_shows_help_with_no_argv() {
  $dimensions 2>&1 | grep -i USAGE
}

it_reads_gifs() {
  gif="$($dimensions ../src/sample.gif)"
  test "$gif" = "../src/sample.gif
  width: 250
  height: 297"
}

it_reads_pngs() {
  png="$($dimensions ../src/sample.png)"
  test "$png" = "../src/sample.png
  width: 405
  height: 239"
}

it_reads_jpgs() {
  jpg="$($dimensions ../src/sample.jpg)"
  test "$jpg" = "../src/sample.jpg
  width: 100
  height: 100"
}
