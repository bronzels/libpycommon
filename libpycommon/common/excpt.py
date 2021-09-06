from time import sleep
from libpycommon.common.mylog import *

def wait_2_exec_times(times, secs_2sleep, func_2wait, *params):
    ret = None
    i = 0
    while i < times:
        try:
            ret = func_2wait(*params)
        except Exception as e:
            logger.debug(str(e))
            pass
        else:
            logger.debug('exception happens, but not caught as Exception')
            pass
        finally:
            if ret is not None:
                break
            sleep(secs_2sleep)
            i += 1
    return ret
