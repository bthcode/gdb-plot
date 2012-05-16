#include <iostream>
#include <complex>
#include <list>
#include <set>
#include <map>
#include <vector>

// Eigen Types
#include <Eigen/Dense>

// Boost types
#include <boost/numeric/ublas/vector.hpp>
#include <boost/numeric/ublas/vector_proxy.hpp>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/numeric/ublas/storage.hpp>

void mod( std::vector< std::complex< double > >& r )
{
    r[0] = std::complex<double>( 3, -1 );
}

// Test sub class 
class TEST2 {
    public:
    TEST2(){};
    ~TEST2(){};
    std::vector< std::complex< double > > x;
};

// Test class
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

    boost::numeric::ublas::vector< double > vx(10,0);
    boost::numeric::ublas::vector< std::complex < double > > vc( 10, 0 );

    double a1[10];

    double * heap_array = ( double * ) malloc( sizeof( double ) * 10 );

    Eigen::MatrixXd m(1,10);
    Eigen::ArrayXcd eigen_complex_array(10);
    Eigen::ArrayXd eigen_double_array(10);

    // Push some data around
    for ( std::size_t ii=0; ii < 10; ii++ )
    {
        v1.push_back( ii * 2*M_PI );
        a1[ii] = 5*ii;
        vx[ii] = ii;
        m(0,ii) = ii * M_PI;
        std::complex<double> q;
        q.real(M_PI *ii);
        q.imag(M_PI *ii);
        v2.push_back( q );
        vc(ii) = q;
        heap_array[ ii ] = M_PI * ii;
        eigen_double_array( ii ) = M_PI * ii;
        eigen_complex_array( ii ) = M_PI * ii + 0.1j;
    }
    

    // Stand up a class
    TEST T;
    T.x = v1;
    T.T2.x = v2;
    std::vector< double > v4;
    T.do_stuff( v4, M_PI );

    mod(T.T2.x);


    std::cout << "Break on line " <<  __LINE__ << " to plot: \n"
              << " .. v1: stl double vector\n"
              << " .. a1: c double array\n"
              << " .. v2: stl complex double vector\n"
              << " ..  m: Eigen double vector\n"
              << " .. vx: Boost Numerics double vector\n"
              << " .. vc: Boost Numerics complex double vector\n"
              << " .. T.x: stl double vector as a member of a class\n"
              << " .. T.T2.x: stl double vector as a member of a class as a member of a class\n"
              << " .. eigen_double_array for an Eigen double array\n"
              << " .. eigen_complex_array for an Eigen complex array\n"
              << std::endl;

    std::cout << "vc: " << vc << std::endl;

    std::cout << "Now try combined plots: plot vx vc T.x T.T2.x " << std::endl;

    free( heap_array );

    return 0;
}
