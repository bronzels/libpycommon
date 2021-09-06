# -*- coding: utf-8 -*-
import chardet
import re
from functools import reduce

def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def is_empty(str):
    if str is None: return True
    stripped = str.strip()
    if len(stripped) == 0: return True
    return False

def is_valid_chinese(str):
    if str is None: return False
    stripped = str.strip()
    if len(stripped) == 0: return False
    return is_chinese(stripped)

def unicode_conv(bytes_input):
    if bytes_input is None: return None
    if isinstance(bytes_input, str): return bytes_input
    d_result = chardet.detect(bytes_input)
    if d_result['encoding'] == 'GB2312':
        return bytes_input.decode('GB2312')
    elif d_result['encoding'] == 'GBK':
        return bytes_input.decode('GBK')
    else:
        return bytes_input.decode('UTF-8')

'''
l_weird_ascii = ['∞', '[', ',', ')']
def is_weird_ascii_4_tablecols(str):
    if str is None: return False
    stripped = str.strip()
    if len(stripped) == 0: return False
    return reduce(lambda x, y: x or y,
                              list(map(lambda x: x in stripped, l_weird_ascii)))
'''
def is_weird_ascii_4_tablecols(str):
    if str is None: return False
    stripped = str.strip()
    if len(stripped) == 0: return False
    return not re.match('^[0-9a-zA-Z_]{1,}$', stripped)

