#!/usr/bin/python

__author__="Brian Hone"


import sys, os, string
import numpy as np
import gdb
import re

def gp_get_data( args ):
    '''
Retrieves data from C/C++ structures into a python numpy array.

Options:
  [in] args - a string containing the items to retreive
            - each element may be some C array time / vector, etc
            - if followed by @, the next argument is n_elements
            - NOTE: '@' followed by n_elements is _required_ for raw pointers or C arrays

  [out] list of numpy arrays

Types Supported:
===== =========
  1. double d[23] 
  2. double d* 
  3. std::vector< double > d
  4. Eigen::Array< double > d
  5. Boost::Numerics::...< double > d
    '''

    data = []
    I = 1j

    print args

    for arg in args:
        n_elements = -1

        # Numbers of elements are denoted with @
        if arg.find( '@' ) >= 0:
            arg_split = arg.split( '@' )
            n_elements = eval( arg_split[-1] )
            arg = arg_split[0]

        ### Try to find the thing to get data from
        try:
            x = gdb.parse_and_eval( arg )
        except:
            print "Couldn't figure out how to access {0}".format(x)
            return

        x_str = str( x.type.strip_typedefs() )

        ########################################
        # BOOST VECTOR
        ########################################
        if x_str.find( "boost" ) >= 0:
            ptr = x['data_']['data_']
            length = x['data_']['size_']
            vals = []
            max_elements = length

            print "capacity = {0}".format( length )
            if n_elements > -1:
                max_elements = min( length, n_elements )
                print "retreiving {0} elements".format( max_elements )

            ## NOT COMPLEX
            if x_str.find( 'complex' ) < 0:
                for i in range( max_elements ):
                    loc = ptr + i
                    vals.append( eval( str(loc.dereference() )) )
                u = np.array( vals )
                data.append(u)
            ## COMPLEX
            else:
                for i in range( max_elements ):
                    loc = ptr + i
                    vals.append( eval( str(loc.dereference()['_M_value'])) )
                u = np.array( vals ) 
                data.append(u)

        ########################################
        # STL VECTOR
        ########################################
        elif x_str.find( "std::vector" ) >= 0:
            ptr = x['_M_impl']['_M_start']
            end = x['_M_impl']['_M_finish']
            vals = []
            length = end - ptr
            max_elements = length

            print "capacity = {0}".format( length )
            if n_elements > -1:
                max_elements = min( length, n_elements )
                print "retreiving {0} elements".format( max_elements )

            element_count = 0
            ## COMPLEX
            if str(x.type).find( 'std::complex' ) >= 0:
                for i in range( max_elements ):
                    vals.append( eval( str( ptr.dereference()['_M_value'] ) ) )
                    ptr = ptr + 1
                u = np.array(vals)
                data.append( u )
            ## Not Complex
            else:
                for i in range( max_elements ):
                    vals.append( eval( str( ptr.dereference() ) ) )
                    ptr = ptr + 1
                u = np.array(vals)
                data.append( u )
        ########################################
        # Eigen
        ########################################
        elif x_str.find( "Eigen::Array" ) >= 0:
            #
            # NOTE: This only works for dynamic Eigen::Array 
            #
            ptr = x['m_storage']['m_data']
            end = x['m_storage']['m_rows']
            vals = []
            max_elements = end

            print "capacity = {0}".format( end )
            if n_elements > -1:
                max_elements = min( max_elements, n_elements )
                print "retreiving {0} elements".format( max_elements )

            if x_str.find("std::complex") >= 0:
                for i in range(max_elements):
                    vals.append( eval( str( ptr.dereference()['_M_value'] ) ) ) 
                    ptr = ptr + 1
                u = np.array( vals ) 
                data.append(u)
            else:
                for i in range(max_elements):
                    vals.append( eval( str( ptr.dereference() ) ) ) 
                    ptr = ptr + 1
                u = np.array( vals ) 
                data.append(u)

        else:
            ##########################################
            # Pointer or Array
            ##########################################
            print "handling raw pointer with n_elements=%s" % ( n_elements )
            end = n_elements
            vals = []

            # Attempt to determine if the data is complex
            is_complex = False
            try:
                _ = x[0]['_M_value']
                is_complex = True
                print "handling data as complex"
            except:
                is_complex = False
                print "handling data as uncomplex"

            if not is_complex:
                for i in range( n_elements ):
                    vals.append( eval( str( x[i] )) )
                u = np.array( vals )
                data.append(u)
            ## COMPLEX
            else:
                for i in range( n_elements ):
                    vals.append( eval( str(x[i]['_M_value'])) )
                u = np.array( vals ) 
                data.append(u)
    return data
# end get_data
