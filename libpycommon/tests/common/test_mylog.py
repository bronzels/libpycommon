# -*- coding: utf-8 -*-
import unittest

from libpycommon.common.mylog import *

class MyclassTest(unittest.TestCase):
    def setUp(self):
        '''
        测试之前的准备工作
        :return:
        '''
        #logger = mylog.get_logger(logging.NOTSET)
        #logger = mylog.get_logger(logging.DEBUG)
        #logger = mylog.get_logger(logging.INFO)

    def tearDown(self):
        '''
        测试之后的收尾
        如关闭数据库
        :return:
        '''
        pass

    def test_class(self):
        logger.debug('debug')
        logger.debug('info')
        logger.warning('warning')
        logger.error('error')
        logger.fatal('fatal')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_class'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
