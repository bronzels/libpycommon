import subprocess
from libpycommon.common.mylog import *

def execute(cmd, err_prompt):
    t_output=subprocess.getstatusoutput(cmd)
    logger.debug('t_output[0]:{}'.format(t_output[0]))
    logger.debug('t_output[1]\n:{}'.format(t_output[1]))
    if t_output[0] != 0:
        raise Exception(err_prompt)
