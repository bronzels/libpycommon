# -*- coding: utf-8 -*-
import unittest

import libpycommon.common.collection as collection
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

    def test_list_intersect(self):
        logger.debug('list_intersect:{}'.format(collection.list_intersect([1, 2, 3], [2, 3, 4])))
        logger.debug('list_intersect_lower:{}'.format(
            collection.list_intersect(['A', 'B', 'C'], ['a', 'b', 'c'], True)))

    def test_list_only_in_first(self):
        logger.debug('list_only_in_first:{}'.format(collection.list_only_in_first([1, 2, 3], [2, 3, 4])))
        logger.debug('list_only_in_first_lower:{}'.format(
            collection.list_only_in_first(['A', 'B', 'C'], ['b', 'c', 'd'], True)))

    def test_dict_get_tuple_key_split(self):
        logger.debug('dict_get_tuple_key_split:{}'.format(collection.dict_get_tuple_key_split({(1, 2):3})))

    def test_dict_chunk(self):
        phones = {
            'a_01': '1200x1500',
            'a_02': '1280x1480',
            'a_03': '1220x1520',
            'a_04': '1240x1540',
            'a_05': '1240x1540',
            'a_06': '1220x1520',
            'a_07': '1240x1540',
            'a_08': '1200x1500',
            'a_09': '1240x1540',
            'a_10': '1240x1540',
            'a_11': '1280x1480',
            'a_12': '1240x1540',
            'a_13': '1220x1520',
            'a_14': '1200x1500',
            'a_15': '1280x1480',
            'a_16': '1240x1540',
            'a_17': '1200x1500',
            'a_18': '1280x1480',
            'a_19': '1240x1540',
            'a_20': '1280x1480',
            'a_21': '1240x1540',
            'a_22': '1280x1480',
        }
        res = collection.dict_chunk_by_size(phones, 10)
        logger.debug(res)
        res = collection.dict_chunk_by_split(phones, 3)
        logger.debug(res)
        res = collection.dict_chunk_by_split(phones, 2)
        logger.debug(res)
        res = collection.dict_chunk_by_split(phones, 4)
        logger.debug(res)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_list_intersect'))
    suite.addTest(MyclassTest('test_list_only_in_first'))
    suite.addTest(MyclassTest('test_dict_get_tuple_key_split'))
    suite.addTest(MyclassTest('test_dict_chunk'))

    runner = unittest.TextTestRunner()
    runner.run(suite)