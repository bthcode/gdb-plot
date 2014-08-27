#!/usr/bin/python

__author__="Brian Hone"


import sys, os, string
import matplotlib.pyplot as plot
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import gdb

from gp_data_extractor import *

class Plotter( gdb.Command ):
    def __init__( self ):
        super( Plotter, self ).__init__("plot", gdb.COMMAND_OBSCURE )

    def invoke( self, arg, from_tty ):
        args = arg.split()

        data = gp_get_data( args )
        fig = plot.figure()
        ax = fig.add_subplot(111)
        ax.grid( True )
        for  u in data:
            if u.dtype.kind == 'c':
                ax.plot( np.abs(u) )
            else:
                ax.plot( u )
        leg = ax.legend((args),
            'upper right', shadow=False)
        leg.get_frame().set_alpha(0.5)
        plot.show()
# end class Plotter

class PlotThreeD( gdb.Command ):
    def __init__( self ):
        super( PlotThreeD, self ).__init__("plot3", gdb.COMMAND_OBSCURE )

    def invoke( self, arg, from_tty ):
        args = arg.split()

        data = gp_get_data( args )
        fig = plot.figure()
        ax = p3.Axes3D( fig )
        ax.grid( True )
        for  u in data:
            if u.dtype.kind == 'c':
                ax.plot( list(range(len(u))), u.real, u.imag )
        leg = ax.legend((args),
            'upper right', shadow=False)
        leg.get_frame().set_alpha(0.5)
        plot.show()
# end class PlotThreeD

   

    
Plotter()
PlotThreeD()
