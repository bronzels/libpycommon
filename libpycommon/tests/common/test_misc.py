# -*- coding: utf-8 -*-
import unittest

from libpycommon.common import misc
from libpycommon.common.mylog import *

from libpycommon.libpycommonkey.me import *

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

    def test_get_env_encrypted(self):
        logger.debug('get_env_encrypted:{}'.format(misc.get_env_encrypted('DB_USER', package_key_res_path)))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_get_env_encrypted'))

    runner = unittest.TextTestRunner()
    runner.run(suite)