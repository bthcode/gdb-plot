## INTRODUCTION ##

This is a set of python gdb plugins to:

  * plot buffers
  * save to a matlab .mat file
  * explore the stack frame
  * send data to ipython for interactive analysis

## OVERVIEW: ##

I have attempted to show support for:

  * c array
  * STL vector
  * Eigen vector
  * Eigen array
  * Boost vector
  * Boost complex vector

## REQUIREMENTS: ##

### Minimum: ###
  * gdb >= 7.0
  * python (tested with 2.7.x and 3.4.x)
  * numpy
  * matplotlib

### Optional: ###
  * scipy ( if you want to save .mat files )

### Requirements for examples: ###

  * Boost::Numerics required for boost example
  * Eigen3 required for eigen example

## HOWTO: ##

  * Directions moved t the README in the repo.  Grab a download or check it out from svn.

## Hack It: ##

Once you get your head around the example code, it's pretty easy to hack it.  Things you could easily do:
  1. Handle more types
  1. Send matrices to images
  1. Add more arguments to the commands - plot a range, plot a column, etc.
  1. Make a single plot command that figures out the type and does the write things.

Enjoy