/**
 * SAMPLE APPLICATION FOR DEMONSTRATING gdb-plot functionality
 *
 * BUILD: g++ -g raw_pointers.cpp -o raw_pointers_example
 * RUN: gdb raw_pointers
 *      (gdb) b 91
 *      (gdb) plot v1
 */

#include <iostream>
#include <complex>
#include <stdlib.h>

int main(void)
{

    double * d = ( double * ) malloc ( 1024 * sizeof(double) ); // raw c pointer
    double e[1024]; // raw c array

    std::complex< double > * x = ( std::complex< double > * ) malloc( 1024 * sizeof(std::complex<double> ) );

    std::complex< float > x2[1024];

    for( std::size_t ii=0; ii < 1024; ii++ )
    {
        d[ii] = 0.25*ii;
        e[ii] = -0.33*ii;
        x[ii].real( d[ii] );
        x[ii].imag( e[ii] );

        x2[ii].real( -d[ii] );
        x2[ii].imag( -e[ii] );
    }

    // ---- print raw pointer ----- //
    std::cout << "d: ";
    for ( std::size_t ii=0; ii < 20; ii ++ )
    {
        std::cout << " " << d[ii];
    }
    std::cout << "...";
    for ( std::size_t ii=1004; ii < 1024; ii ++ )
    {
        std::cout << " " << d[ii];
    }
    std::cout << std::endl;

    // ---- print raw array ----- //
    std::cout << "e: ";
    for ( std::size_t ii=0; ii < 20; ii ++ )
    {
        std::cout << " " << e[ii];
    }
    std::cout << "...";
    for ( std::size_t ii=1004; ii < 1024; ii ++ )
    {
        std::cout << " " << e[ii];
    }
    std::cout << std::endl;


    std::cout << "\n\n---------------------------------------------\n\n"
              << "Break on line " <<  __LINE__ << " to plot: \n"
              << " plot d@1024: malloc'd pointer\n"
              << " plot e@1024: c stack array\n"
              << " plot x@1024: c complex double malloc'd pointer\n"
              << std::endl;

    std::cout << " .. Now try combined plots: plot d 1024 e 1024 " << std::endl;

    free(d);
    free(x);


    return 0;
}
