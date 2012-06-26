INTRODUCTION:
============

This is a set of utils for:

- plotting from the gdb command line
- saving c data to .mat files from gdb command line
- sending data to an iPython engine from the gdb command line

WARNING:
=======

It is __not__ meant to be a perfect, working system.  It is a template that will get you started hacking your own plotters

OVERVIEW:
========

I have attempted to show support for:

- c array
- STL vector
- Eigen vector, Eigen array
- Boost vector
- Boost complex vector

REQUIREMENTS:
============
python, numerics, matplotlib, scipy
gdb >= 7.0

The examples are divided up so you only need the dependencies for the example you want to run:

- stl_examples : gcc/g++ and libstdc++
- boost_numerics_examples : boost numerics (boost-devel)
- eigen_examples : eigen3 library ( eigen3-devel )

HOWTO:
=====
1. Configure gdb
     add the lines in gdbinit to ~/.gdbinit, fix the paths
     NOTE: REPLACE 'THIS DIRECTORY' with the root directory of this repository

2. Build any examples you want:

   cd examples
   STL Example            : g++ -g stl_example.cpp -o stl_example
   Boost Numerics Example : g++ -g boost_numerics_example.cpp -o boost_example
   Eigen3 Example         : g++ -g -I/usr/include/eigen3 eigen_example.cpp -o eigen_example

3. Debug the examples

    NOTE: each example will print out a useful line to break on, and things you may want to plot.  Just run it to get that printout.

    gdb stl_example              # launch example program
    b 91                         # give it a break point and run it
    r
    plot v1 a1                  # plot a bunch of data of different types
    savemat mymatfile v1 a1     # Save array eca2 to a matlab .mat file 

4. Send data to ipython

   # in another shell:  
   ipython kernel --pylab        # start an ipython server instance
   # in a second shell
   ipython console --existing=<connection string>  # connection string here ( spit out by previous command )
   # in gdb
   send <connection number> data   # send data to ipython
   

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

(gdb) show_frame
{'T': ['TEST', 'local_computation', 0],
 'a1': ['double [10]', 'local_computation', 0],
 'eca2': ['Eigen::ArrayXcd', 'local_computation', 0],
 'eda2': ['Eigen::ArrayXd', 'local_computation', 0],
 'eigen_complex_array': ['Eigen::ArrayXcd', 'local_computation', 0],
 'eigen_double_array': ['Eigen::ArrayXd', 'local_computation', 0],
 'heap_array': ['double *', 'local_computation', 0],
 'm': ['Eigen::MatrixXd', 'local_computation', 0],
 'v1': ['std::vector<double, std::allocator<double> >',
        'local_computation',
        10],
 'v2': ['std::vector<std::complex<double>, std::allocator<std::complex<double> > >',
        'local_computation',
        10],
 'v4': ['std::vector<double, std::allocator<double> >',
        'local_computation',
        5],
 'vc': ['boost::numeric::ublas::vector<std::complex<double>, boost::numeric::ublas::unbounded_array<std::complex<double>, std::allocator<std::complex<double> > > >',
        'local_computation',
        10],
 'vx': ['boost::numeric::ublas::vector<double, boost::numeric::ublas::unbounded_array<double, std::allocator<double> > >',
        'local_computation',
        10]}





Enjoy

