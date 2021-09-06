# -*- coding: utf-8 -*-
import unittest

import libpycommon.common.mystring as mystring
from libpycommon.common.mylog import *

class MyclassTest(unittest.TestCase):
    def setUp(self):
        '''
        测试之前的准备工作
        :return:
        '''

    def tearDown(self):
        '''
        测试之后的收尾
        如关闭数据库
        :return:
        '''
        pass

    def test_is_valid_chinese(self):
        logger.debug('is_valid_chinese_x哈哈:{}'.format(mystring.is_valid_chinese('x哈哈')))
        logger.debug('is_valid_chinese_xyz:{}'.format(mystring.is_valid_chinese('xyz')))
        logger.debug('is_valid_chinese_   :{}'.format(mystring.is_valid_chinese('   ')))
        logger.debug('is_valid_chinese_  你好 :{}'.format(mystring.is_valid_chinese('  你好 ')))
        logger.debug('is_valid_chinese_None:{}'.format(mystring.is_valid_chinese(None)))
        logger.debug('is_valid_chinese_:{}'.format(mystring.is_valid_chinese('')))

    def test_is_weird_ascii_4_tablecols(self):
        logger.debug('is_weird_ascii_4_tablecols_abc:{}'.format(mystring.is_weird_ascii_4_tablecols('abc')))
        logger.debug('is_weird_ascii_4_tablecols_abc-:{}'.format(mystring.is_weird_ascii_4_tablecols('abc-')))
        logger.debug('is_weird_ascii_4_tablecols_abcABC123:{}'.format(mystring.is_weird_ascii_4_tablecols('abcABC123')))
        logger.debug('is_weird_ascii_4_tablecols_abc_:{}'.format(mystring.is_weird_ascii_4_tablecols('abc_')))
        logger.debug('is_weird_ascii_4_tablecols_abc]:{}'.format(mystring.is_weird_ascii_4_tablecols('abc]')))
        logger.debug('is_weird_ascii_4_tablecols_$$涂彬老师:{}'.format(mystring.is_weird_ascii_4_tablecols('$$涂彬老师')))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_is_valid_chinese'))

    runner = unittest.TextTestRunner()
    runner.run(suite)