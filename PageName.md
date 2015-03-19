## INTRODUCTION ##

This is a set of python gdb plugins to:

  * plot buffers
  * save to a matlab .mat file
  * explore the stack frame

## WARNING ##

It is not meant to be a perfect, working system.  It is a template that will get you started hacking your own plotters

## OVERVIEW: ##

I have attempted to show support for:

  * c array, c pointer array
  * STL vector
  * Eigen vector
  * Eigen array
  * Boost vector
  * Boost complex vector

## REQUIREMENTS: ##

  * python
  * numerics
  * matplotlib
  * scipy
  * gdb >= 7.0

To use the example, you'll need boost-devel and eigen3-devel packages

## HOWTO: ##

##### Configure GDB #####

> add the lines in gdbinit to ~/.gdbinit, fix the paths

##### Build the Example #####
> g++ example.cpp -I/usr/include/eigen3 -o example -g

##### Debug the Example #####

```
    gdb test                 # launch example program
    (gdb) b 106                        # give it a break point and run it
    (gdb) r
    (gdb) plot v1 a1 vc m             # plot a bunch of data of different types
    (gdb) plot3 eca2                  # Plot a complex array in 3D
    (gdb) savemat mymatfile eca2      # Save array eca2 to a matlab .mat file
    (gdb) show_frame                  # Show a nice printout of the current stack frame
```

##### Plot in GDB #####

./test
```
Break on line 40 to plot r_data, an stl vector passed by reference
Break on line 84 to plot: 
 .. v1: stl double vector
 .. a1: c double array
 .. v2: stl complex double vector
 ..  m: Eigen double vector
 .. vx: Boost Numerics double vector
 .. vc: Boost Numerics complex double vector
 .. T.x: stl double vector as a member of a class
 .. T.T2.x: stl double vector as a member of a class as a member of a class

Now try combined plots: plot vx vc T.x T.T2.x 
```

##### Raw Pointers Example #####
Raw pointers must have a size passed in with them via 'varname@size'
```
 gdb raw_pointers_example
 .. b 52
 .. r
 .. plot d@1024
```

##### Hack It #####
> The examples here are really simple.  It's just not entirely intuitive.  Things you could easily do:
    1. Handle more types
> > 2. Send matrices to images
> > 3. Add more arguments to the commands - plot a range, plot a column, etc.
> > 4. Make a single plot command that figures out the type and does the write things.

Enjoy