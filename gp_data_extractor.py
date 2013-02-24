#!/usr/bin/python

__author__="Brian Hone"


import sys, os, string
import numpy as np
import gdb
import re

def gp_get_data( args ):
    data = []
    I = 1j
    for arg in args:
        n_elements = 1
        # Numbers of elements are denoted with @
        if arg.find( '@' ) >= 0:
            arg_split = arg.split( '@' )
            n_elements = eval( arg_split[-1] )
            arg = arg_split[0]
        # If we're dealing with sub-structures, descend down
        if arg.find('.') >=0 :
            arg_split = arg.split( '.' )
            x = gdb.selected_frame().read_var(arg_split[0])
            for i in arg_split[1:]:
                x = x[i]
        # Else, just get the data
        else:
            print arg
            try: ## try a stack variable
                x = gdb.selected_frame().read_var(arg)
            except: ## try a class member
                x = gdb.selected_frame().read_var("this").dereference()[arg]
        x_str = str(x)
        

        # Search regexes for matching raw pointer and array types
        types = [ 'int', 'float', 'double', 'short' ]
        ptr_types = [ r'(%s *)' % t for t in types ]
        arr_types = [ r'%s \[\w+\]' % t for t in types ]
        ptr_matches = [ re.search( ptr_type, str(x.type) ) for ptr_type in ptr_types ]
        arr_matches = [ re.search( arr_type, str(x.type) ) for arr_type in arr_types ]

        ##########################################
        # Pointer or Array
        ##########################################
        if not all( v is None for v in ptr_matches ) or not all( v is None for v in arr_matches ):
            print "handling raw pointer with n_elements=%s" % ( n_elements )
            ptr = x
            end = n_elements
            vals = []
            for i in range(end):
                vals.append( eval( str(ptr[i]) ) )
            u = np.array(vals)
            data.append(u)

        ########################################
        # BOOST VECTOR
        ########################################
        elif x_str.find( "boost" ) >= 0:
            ptr = x['data_']['data_']
            size = x['data_']['size_']
            vals = []
            ## NOT COMPLEX
            if x_str.find( 'std::complex' ) < 0:
                for i in range( size ):
                    loc = ptr + i
                    vals.append( eval( str(loc.dereference() )) )
                u = np.array( vals )
                data.append(u)
            ## COMPLEX
            else:
                for i in range( size ):
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
            ## COMPLEX
            if str(x.type).find( 'std::complex' ) >= 0:
                while ptr != end:
                    vals.append( eval( str( ptr.dereference()['_M_value'] ) ) )
                    ptr = ptr + 1
                u = np.array(vals)
                data.append( u )
            ## Not Complex
            else:
                while ptr != end:
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
            if x_str.find("std::complex") >= 0:
                ptr = x['m_storage']['m_data']
                end = x['m_storage']['m_rows']
                vals = []
                for i in range(end):
                    vals.append( eval( str( ptr.dereference()['_M_value'] ) ) ) 
                    ptr = ptr + 1
                u = np.array( vals ) 
                data.append(u)
            else:
                ptr = x['m_storage']['m_data']
                end = x['m_storage']['m_rows']
                vals = []
                for i in range(end):
                    vals.append( eval( str( ptr.dereference() ) ) ) 
                    ptr = ptr + 1
                u = np.array( vals ) 
                data.append(u)
        ########################################
        # Unknown, try parsing the string
        ########################################
        else:
            brace_pos = x_str.find('{') 
            brace_pos2 = x_str.find('}')
            x_str = '[ %s ]' % x_str[ brace_pos+1:brace_pos2]
            s = eval( '%s' % x_str )
            u = np.array( s ) 
            data.append(u)

    return data
# end get_data
