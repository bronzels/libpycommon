import logging
import sys
import os

_nameToLevel = {
    'critical': logging.CRITICAL,
    'fatal': logging.FATAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG,
    'notset': logging.NOTSET,
}

def get_logger(level=None):
    logger = logging.getLogger('mylog')
    if level is None:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(level)
    format_str = logging.Formatter(
        '%(asctime)s - %(processName)s - %(threadName)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s', '%Y-%m-%d %H:%M:%S')
        #'%(processName)s - %(threadName)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s', None)
    sh = logging.StreamHandler(stream=sys.stdout)  # output to standard output
    sh.setFormatter(format_str)
    logger.addHandler(sh)
    return logger

def get_level_from_name(level_name):
    return _nameToLevel.get(level_name)

def get_topmodname():
    mod = sys.modules['__main__']
    file = getattr(mod, '__file__', None)
    modname = os.path.basename(os.path.dirname(file))
    return modname

#logger = get_logger()
logger = get_logger(logging.DEBUG)
#logger = get_logger(logging.WARNING)
