#!/usr/bin/python

__author__="Brian Hone"


import sys, os, string, pprint
import gdb

sym_types = {
    gdb.SYMBOL_LOC_UNDEF : "undefined",
    gdb.SYMBOL_LOC_CONST : "constant_int",
    gdb.SYMBOL_LOC_STATIC : "fixed_address",
    gdb.SYMBOL_LOC_REGISTER : "register",
    gdb.SYMBOL_LOC_ARG : "argument",
    gdb.SYMBOL_LOC_REF_ARG : "ref_arg",
    gdb.SYMBOL_LOC_REGPARM_ADDR : "register_pointer",
    gdb.SYMBOL_LOC_LOCAL : "local",
    gdb.SYMBOL_LOC_TYPEDEF : "local_typedef",
    gdb.SYMBOL_LOC_BLOCK : "block",
    gdb.SYMBOL_LOC_CONST_BYTES : "byte_sequence",
    gdb.SYMBOL_LOC_UNRESOLVED : "unresolved_address",
    gdb.SYMBOL_LOC_OPTIMIZED_OUT : "optimized_out",
    gdb.SYMBOL_LOC_COMPUTED : "local_computation"
}

def describe( var, sym ):
    ''' Gather information about a given variable '''
    ## Get Type
    var_type = str(var.type)
    size = 0
    ## Attempt to figure out its size, base type, min val, max val
    if var_type.find( 'std::vector' ) >= 0:
        ptr = var['_M_impl' ]['_M_start' ]
        end = var['_M_impl' ]['_M_finish' ]
        size = end - ptr
        pass
    elif var_type.find( 'boost::numeric::ublas::vector' ) >= 0:
        size = var['data_']['size_']
    elif var_type.find( 'std::map' ) >= 0:
        pass
    elif var_type.find( 'std::list' ) >= 0:
        pass
    elif var_type.find( 'Eigen' ) >= 0:
        pass
    elif var_type.find( '[' ) >= 0 and var_type.find( ']' ) > var_type.find( '[' ):
        pass
    

    return [ str(var_type), sym_types[ sym.addr_class ], eval(str(size)) ]
# end describe


class ShowFrame( gdb.Command ):
    def __init__( self ):
        super( ShowFrame, self ).__init__("show_frame", gdb.COMMAND_OBSCURE )
    # def __init__

    def invoke( self, arg, from_tty ):
        ###
        # Get to the frame and block we want
        #
        frame =  gdb.selected_frame()
        block = gdb.selected_frame().block()
        frame_vars = {}
        
        ###
        # Walk through the symbols in the block
        #
        for sym in block:
            ###
            # Retreive the symbols from the frame
            #
            var = frame.read_var( sym )
            frame_vars[ str(sym) ] = describe( var, sym )
        print pprint.pformat( frame_vars )

    # def invoke
         
# end class StemPlotter

   
ShowFrame()
