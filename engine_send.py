from IPython.lib.kernel import find_connection_file
from IPython.zmq.blockingkernelmanager import BlockingKernelManager
import sys, os, string
import numpy as np
import gdb
from gp_data_extractor import *


class Sender( gdb.Command ):


    def __init__( self ):
        super( Sender, self ).__init__("send", gdb.COMMAND_OBSCURE )


    def invoke( self, arg, from_tty ):
        con_id = string.split( arg )[0]
        args = string.split( arg )[1:]
        # this is a helper method for turning a fraction of a connection-file name
        # into a full path.  If you already know the full path, you can just use that
        cf = find_connection_file(con_id)

        self.km = BlockingKernelManager(connection_file=cf)
        # load connection info and init communication
        self.km.load_connection_file()
        self.km.start_channels()

        data = gp_get_data( args )
        print data
        for i in range( len(data) ):
            name = args[i]
            u    = data[i]
            cmd = '%s=np.array(%s)' % ( name, u.tolist() )
            self.km.shell_channel.execute( cmd )

        del(self.km)
# end class Sender


Sender()
