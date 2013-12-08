/**
 * SAMPLE APPLICATION FOR DEMONSTRATING gdb-plot functionality
 *
 * BUILD: g++ -g raw_pointers.cpp -o raw_pointers_example
 * RUN: gdb raw_pointers
 *      (gdb) b 91
 *      (gdb) plot v1
 */

#include <iostream>
#include <stdlib.h>

typedef double * double_vec;

int main(void)
{

    double * d = ( double * ) malloc ( 1024 * sizeof(d) ); // raw c pointer
    double e[1024]; // raw c array

    double_vec dv = ( double_vec ) malloc ( 1024 * sizeof(double * ) );

    for( std::size_t ii=0; ii < 1024; ii++ )
    {
        d[ii] = 0.25*ii;
        e[ii] = -0.33*ii;
        dv[ii] = -0.44*ii;
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


    std::cout << "Break on line " <<  __LINE__ << " to plot: \n"
              << " .. d@1024: malloc'd pointer\n"
              << " .. e@1024: c stack array\n"
              << " .. dv@1024: double * malloc'd pointer typedef'd to a double_vec\n"
              << std::endl;

    std::cout << " .. Now try combined plots: plot d 1024 e 1024 " << std::endl;

    free(d);


    return 0;
}
