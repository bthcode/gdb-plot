#!/usr/bin/python

__author__="Brian Hone"

import sys, os, string
import numpy as np
import scipy.io as sio
import gdb
from gp_data_extractor import *

class MatSaver( gdb.Command ):
    def __init__( self ):
        super( MatSaver, self ).__init__("savemat", gdb.COMMAND_OBSCURE )

    def invoke( self, arg, from_tty ):
        args = string.split( arg )
        fname = args[0]
        raw_data = gp_get_data( args[1:] )
        data = {}
        for i in range( len( raw_data ) ):
            key = args[i+1]
            val = raw_data[i]
            data[ key ] = val
            print "Saving %s" % key   
        sio.savemat( fname, data )
# end class Plotter

MatSaver()
