__author__ = 'moonkey'

import platform
import socket

# ##################################
##########  SERVER  ###############
###################################
model_root = '/opt/'



# easy hack to differ from local and server
local_name = platform.node()
if not local_name:
    local_name = socket.gethostname()
if 'mac' in local_name.lower():
    ###################################
    ##########    MAC   ###############
    ###################################
    model_root = '/opt/'