/**
 * SAMPLE APPLICATION FOR DEMONSTRATING gdb-plot functionality
 *
 * BUILD: g++ -g boost_numerics_example.cpp -o boost_example
 * RUN: gdb boost_example
 *      (gdb) b 91
 *      (gdb) plot vx vc
 */

#include <iostream>
#include <complex>
#include <list>
#include <set>
#include <map>
#include <vector>

// Boost types
#include <boost/numeric/ublas/vector.hpp>
#include <boost/numeric/ublas/vector_proxy.hpp>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/numeric/ublas/storage.hpp>


int main(void)
{

    boost::numeric::ublas::vector< double > vx(10,0);
    boost::numeric::ublas::vector< std::complex < double > > vc( 10, 0 );

    // Push some data around
    for ( std::size_t ii=0; ii < 10; ii++ )
    {

        vx[ii] = ii;
        std::complex<double> q;
        q.real(M_PI *ii);
        q.imag(M_PI *ii);
        vc(ii) = q;
    }


    std::cout << "Break on line " <<  __LINE__ << " to plot: \n"
              << " .. vx: Boost Numerics double vector\n"
              << " .. vc: Boost Numerics complex double vector\n"
              << std::endl;

    std::cout << "Now try combined plots: plot vx vc" << std::endl;

    return 0;
}
