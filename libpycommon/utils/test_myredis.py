# -*- coding: utf-8 -*-
import unittest
import os
from libpycommon.common.mylog import *
from libpycommon.common.myredis import Redis_conn
from libpycommon.libpycommonkey.me import *
class MyclassTest(unittest.TestCase):
    def setUp(self):
        '''
        测试之前的准备工作
        :return:
        '''
        os.environ['REDIS_HOST']="192.168.0.85"
        os.environ['REDIS_PORT']="16379"
        os.environ['REDIS_MAX_CONN']="10"
        os.environ['REDIS_PASSWD']='EfTjF6f8uXKKPxl2SiucXCEJzO1tdzY/rwszWt6O1cO89sLQRQbN5nn7kRXwcd9hxlAMhhTtCztS2hPoDzD2bawoV4OtT8IT2X3Etb1Urxs9aV4iNS6doqkSShutiugZhCQboWrfsM3FEZEFChQv4+Zsjckw2DFbG1/Fl9+s/K0='

    def tearDown(self):
        '''
        测试之后的收尾
        如关闭数据库
        :return:
        '''
        pass

    def test01_get_r(self):
        redis_conn=Redis_conn(package_key_res_path)
        r=redis_conn.getR()
        r.set('libpycommon:test_redis:k','value')
        self.assertEqual(r.get('libpycommon:test_redis:k').decode(),'value')
        r.delete('libpycommon:test_redis:k')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test01_get_r'))
    runner = unittest.TextTestRunner()
    runner.run(suite)