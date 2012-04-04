INTRODUCTION:
============

This is a set of utils for plotting from gdb commmand line.

WARNING:
=======

It is __not__ meant to be a perfect, working system.  It is a template that will get you started hacking your own plotters

OVERVIEW:
========

I have attempted to show support for:

- c array
- STL vector
- Eigen vector
- Boost vector
- Boost complex vector

REQUIREMENTS:
============
python, numerics, matplotlib
gdb >= 7.0

To use the example, you'll need boost-devel and eigen3-devel packages

HOWTO:
=====
1. Configure gdb
     add the lines in gdbinit to ~/.gdbinit, fix the paths

2. Build the example 
     g++ example.cpp -I/usr/include/eigen3 -o example -g

3. Debug the example
    gdb example                 # launch example program
    b 94                        # give it a break point and run it
    r
    plot v1 a1 vc m             # plot a bunch of data of different types

3. Hack it
    The examples here are really simple.  It's just not entirely intuitive.  Things you could easily do:
        1. Handle more types
        2. Send matrices to images
        3. Add more arguments to the commands - plot a range, plot a column, etc.
        4. Make a single plot command that figures out the type and does the write things.

OTHER USEFUL STUFF:
==================

savemat - saves arbitrary buffers as a .mat file [ requires scipy ]
showframe - stack frame explorer


Enjoy

