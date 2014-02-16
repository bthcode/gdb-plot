/**
 * SAMPLE APPLICATION FOR DEMONSTRATING gdb-plot functionality
 *
 * BUILD: g++ -g stl_example.cpp -o stl_example
 * RUN: gdb stl_example
 *      (gdb) b 91
 *      (gdb) plot v1
 */

#include <iostream>
#include <complex>
#include <list>
#include <set>
#include <map>
#include <vector>
#include <stdlib.h>

typedef std::vector< double > double_vec;

/**
 * Modify a vector - demonstrates plotting reference variables
 */
void mod( std::vector< std::complex< double > >& r )
{
    r[0] = std::complex<double>( 3, -1 );
}

/**
 * Simple class for demonstrating plotting class members
 */
class TEST2 {
    public:
    TEST2(){};
    ~TEST2(){};
    std::vector< std::complex< double > > x;
};

class TEST {
    public:
    TEST(){};
    ~TEST(){};
    std::vector< double > x;
    double y;
    int do_stuff( std::vector< double >& r_data, double d )
    {
        r_data.resize(5);
        for ( std::size_t ii=0; ii < r_data.size(); ii++ )
        {
            r_data[ii] = double(ii) * M_PI;
        }
        std::cout << "Break on line " << __LINE__ << " to plot r_data, an stl vector passed by reference" << std::endl;
        return 0;
    }
    TEST2 T2;
};


int main(void)
{

    // A bunch of different data types
    std::vector< double > v1;
    std::vector< std::complex<double> > v2;
    double a1[10];

    // Push some data around
    for ( std::size_t ii=0; ii < 10; ii++ )
    {
        v1.push_back( ii * 2*M_PI );
        a1[ii] = 5*ii;

        std::complex<double> q;
        q.real(M_PI *ii);
        q.imag(M_PI *ii);
        v2.push_back( q );


    }


    // Stand up a class
    TEST T;
    T.x = v1;
    T.T2.x = v2;
    std::vector< double > v4;
    T.do_stuff( v4, M_PI );

    mod(T.T2.x);

    double_vec dv = v1;


    std::cout << "\n\n-------------------------------------------\n\n"
              << "Break on line " <<  __LINE__ << " to plot: \n"
              << " .. v1: stl double vector\n"
              << " .. dv: stl double vector typedef'd to a double_vec\n"
              << " .. a1@10: c double array\n"
              << " .. v2: stl complex double vector\n"
              << " .. T.x: stl double vector as a member of a class\n"
              << " .. T.T2.x: stl double vector as a member of a class as a member of a class\n"
              << std::endl;

    std::cout << " .. Now try combined plots: plot v v2 T.x T.T2.x " << std::endl;


    return 0;
}
