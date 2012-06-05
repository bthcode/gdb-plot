###############################################
# Stupid script to build examples - 
#   These examples are thin samples and 
#   don't really warrant a build system
###############################################

echo "Building a few examples - "
echo "  - If any build fails, that's probably ok - these are just examples"

echo "Building stl example..."
g++ examples/stl_example.cpp -g -o examples/stl_example
echo " .. debug it with 'gdb examples/stl_example'"

echo 
echo "Building Boost::numerics example..."
g++ examples/boost_numerics_example.cpp -g -o examples/boost_example
echo " .. debug it with 'gdb examples/boost_example'"

echo
echo "Building Eigen3 example..."
g++ -g -I/usr/include/eigen3 examples/eigen_example.cpp -o examples/eigen_example
echo " .. debug it with 'gdb examples/eigen_example'"

