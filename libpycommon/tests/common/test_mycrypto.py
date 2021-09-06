# -*- coding: utf-8 -*-
import unittest

from libpycommon.common import mycrypto
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

    def test_create_key_pair(self):
        mycrypto.create_key_pair(package_key_abs_path)

    def test_encrypt(self):
        logger.debug('encrypt:{}'.format(mycrypto.encrypt('Dev@#0907Dba', package_key_res_path)))

    def test_decrypt(self):
        logger.debug('decrypt:{}'.format(mycrypto.decrypt('fV7cgAJEo4N01VAvpZbAbgJ0v6Bt0YwmElRCegN64FIr47dNjhd61GZ1jWkWokcXABZ6J1WOyK+oHHF7+vMRN3ETqi6dXGxzjeNJJEyQmRHGDfXGxZBvamxWtUoda2QRm05G7tyIjpBMVyv0YWBPkH6lp9QZUSQQgUuz1yxIqnM=', package_key_res_path)))

    def test_sign(self):
        logger.debug('sign:{}'.format(mycrypto.sign('你好，这是一篇文章', package_key_res_path)))

    def test_verify(self):
        logger.debug('verify:{}'.format(mycrypto.verify('你好，这是一篇文章', 'qN5UaevyvVFmUB6es4qnPxhcrq9/Ui3ce1zuXCmpWxz1NF6UnXYUxhWU6dJGwn8VoeBN6wuc6p2Kl7xw1cbOMbmYjMSktiROEZkI8EhZNugegPeMrxL5P4/bgGBF3yqAFLP7DZ37B7gzZH1r1p08t23xdswUrl6hxhFZ4cAECR0=', package_key_res_path)))
        logger.debug('verify:{}'.format(mycrypto.verify('你好，这是一篇好文章', 'qN5UaevyvVFmUB6es4qnPxhcrq9/Ui3ce1zuXCmpWxz1NF6UnXYUxhWU6dJGwn8VoeBN6wuc6p2Kl7xw1cbOMbmYjMSktiROEZkI8EhZNugegPeMrxL5P4/bgGBF3yqAFLP7DZ37B7gzZH1r1p08t23xdswUrl6hxhFZ4cAECR0=', package_key_res_path)))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    #suite.addTest(MyclassTest('test_create_key_pair'))
    #suite.addTest(MyclassTest('test_encrypt'))
    #suite.addTest(MyclassTest('test_decrypt'))

    runner = unittest.TextTestRunner()
    runner.run(suite)