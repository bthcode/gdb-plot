/**
 * SAMPLE APPLICATION FOR DEMONSTRATING gdb-plot functionality
 *
 * BUILD: g++ -g -I/usr/include/eigen3 eigen_example.cpp -o eigen_example
 * RUN: gdb eigen_example
 *      (gdb) b 51
 *      (gdb) plot sin_array cos_array
 */

#include <iostream>
#include <complex>
#include <list>
#include <set>
#include <map>
#include <vector>

// Eigen Types
#include <Eigen/Dense>


int main(void)
{

    Eigen::MatrixXd m(1,10);
    Eigen::ArrayXcd eigen_complex_array(10);
    Eigen::ArrayXd eigen_double_array(10);
    Eigen::ArrayXcd eca2(2048);
    Eigen::ArrayXd  eda2(2048);
    Eigen::ArrayXd  sin_array(2048);
    Eigen::ArrayXd  cos_array(2048);
    Eigen::ArrayXd  tan_array(2048);

    // Push some data around
    for ( std::size_t ii=0; ii < 10; ii++ )
    {
        m(0,ii) = ii * M_PI;
        eigen_double_array( ii ) = M_PI * ii;
        eigen_complex_array( ii ) = M_PI * ii + 0.1j;
    }

    for ( std::size_t ii=0; ii < eca2.size(); ii++ )
    {
        eda2(ii) = ii * 0.01;
        eca2(ii) = ii + 0.1j;
    }

    sin_array = eda2.sin();
    cos_array = eda2.cos();
    tan_array = eda2.tan();
    
    std::cout << "\n\n----------------------------------------\n\n"
              << "Break on line " <<  __LINE__ << " to plot: \n"
              << "  plot eda2 for an Eigen double array\n"
              << "  plot eca2 for an Eigen complex array\n"
              << "  plot sin_array cos_array  tan_array for trig plots\n"
              << std::endl;

    return 0;
}
