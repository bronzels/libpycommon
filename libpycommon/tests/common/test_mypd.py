# -*- coding: utf-8 -*-
import unittest
import pandas as pd

import libpycommon.common.mypd as mypd
from libpycommon.common.mylog import *

class MyclassTest(unittest.TestCase):
    def setUp(self):
        '''
        测试之前的准备工作
        :return:
        '''
        data = {
            'name': ['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'qianqi', 'zhangsan'],
            'age': [18, 19, 20, 21, 22, 23],
            'city': ['beijing', 'shanghai', 'guangzhou', 'nanjing', 'changsha', 'wuhan'],
            'sex': ['man', 'women', 'man', 'women', 'man', 'women']
        }
        self.df = pd.DataFrame(data)

    def tearDown(self):
        '''
        测试之后的收尾
        如关闭数据库
        :return:
        '''
        pass

    def test_get_dict_2_list(self):
        logger.debug('get_dict_2_list:{}'.format(mypd.get_dict_2_list(self.df, 'sex', 'name')))

    def test_get_dict(self):
        logger.debug('get_dict:{}'.format(mypd.get_dict(self.df, 'name', 'age')))

    def test_get_df_trimmed(self):
        data_space = {
            'name': ['zhangsan_space      ', 'lisi', 'wangwu', 'zhaoliu', 'qianqi', 'zhangsan'],
            'age': [18, 19, 20, 21, 22, 23],
            'city': [None, '      space_shanghai', 'guangzhou', 'nanjing', 'changsha', 'wuhan'],
            'sex': ['man', 'women', '1       man', 'women', 'man', 'women']
        }
        df_space = pd.DataFrame(data_space)
        logger.debug(df_space)
        mypd.get_df_trimmed(df_space)
        logger.debug(df_space)

    def test_get_df_merged(self):
        data = {
            'name': ['zhangsan_space      ', 'lisi', 'wangwu', 'zhaoliu', 'qianqi', 'zhangsan'],
            'age': [18, 19, 20, 21, 22, 23],
            'city': [None, '      space_shanghai', 'guangzhou', 'nanjing', 'changsha', 'wuhan'],
            'sex': ['man', 'women', '1       man', 'women', 'man', 'women']
        }
        df1 = pd.DataFrame(data)
        df2 = pd.DataFrame(data)
        df3 = pd.DataFrame(data)
        logger.debug(mypd.get_df_merged([df1, df2, df3]))
        logger.debug(df1)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_get_dict_2_list'))
    suite.addTest(MyclassTest('test_get_dict'))
    suite.addTest(MyclassTest('test_get_df_trimmed'))
    suite.addTest(MyclassTest('test_get_df_merged'))

    runner = unittest.TextTestRunner()
    runner.run(suite)