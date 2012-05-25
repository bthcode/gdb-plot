#!/usr/bin/python

__author__="Brian Hone"


import sys, os, string, time, pprint, subprocess
import numpy as np
import matplotlib.pyplot as plot
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import gdb

def get_data( args ):
    data = []
    I = 1j
    for arg in args:
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
        ########################################
        # BOOST VECTOR
        ########################################
        if x_str.find( "boost" ) >= 0:
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
                    vals.append( ptr.dereference() ) 
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

class Plotter( gdb.Command ):
    def __init__( self ):
        super( Plotter, self ).__init__("plot", gdb.COMMAND_OBSCURE )

    def invoke( self, arg, from_tty ):
        args = string.split( arg )

        data = get_data( args )
        fig = plot.figure()
        ax = fig.add_subplot(111)
        ax.grid( True )
        for  u in data:
            if u.dtype.kind == 'c':
                ax.plot( np.abs(u) )
            else:
                ax.plot( u )
        plot.show()
# end class Plotter

class PlotThreeD( gdb.Command ):
    def __init__( self ):
        super( PlotThreeD, self ).__init__("plot3", gdb.COMMAND_OBSCURE )

    def invoke( self, arg, from_tty ):
        args = string.split( arg )

        data = get_data( args )
        fig = plot.figure()
        ax = p3.Axes3D( fig )
        ax.grid( True )
        for  u in data:
            if u.dtype.kind == 'c':
                ax.plot( range(len(u)), u.real, u.imag )
        plot.show()
# end class PlotThreeD

   

    
Plotter()
PlotThreeD()
