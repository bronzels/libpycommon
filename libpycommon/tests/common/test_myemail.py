# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import unittest
import os
from libpycommon.common.mylog import *
from libpycommon.inoutput.myemail import Email_sender
from libpycommon.libpycommonkey.me import *
class MyclassTest(unittest.TestCase):
    def setUp(self):
        '''
        测试之前的准备工作
        :return:
        '''
        os.environ['SMTP_SMARTHOST']="smtp.mxhichina.com"
        os.environ['SMTP_SMARTPORT']="465"
        os.environ['SMTP_AUTH_USERNAME']='rntHyO+rAEpmOO+32A8Leu2lMZ3a3nox52IJd2ssfnG0hIwOil6UkNaVrfM7C6PcnFrFIOQY2A82QtJf1EpG0WnSGTcl0+XAL40AnAQqXoyDB6CBY3By/tMrBEfJZhCtMTtuBVymsljnu5RehMxjqrEIz5awxUmg8tZw1Py6bcE='
        os.environ['SMTP_AUTH_PASSWORD']= 'Ob3QFW/NDDK0yVLturor9LYrT86cF8/JEUzxMjA08EG2wVy5/Yjls+hLhklCbO2S+S8t0HKUjdT/rEgzz+QS+gV1OBOsk+B2g4TnTE2ctp/tGQXFXg8+rxb/xSFkrmFSHffFQxkTIaOeX9fQ18GyEFNv4ikjoIuNigPadWJSQHE='
        os.environ['SMTP_FROM']='gRvlw2BZJlHsof3PZ6xG60E6EJLe6iI9STrEvonH9sjrh685QNAG7BjxDyrlzCbfi1KZay5OOp9dtYQ7mOgBElM1UJkTCH3rnB52y+JgDy6/uhTxoo61zwWF0X8SJ+ojf2QfSfxfXVEysME/AVEQ/FYUKnYbsEtKAFAFrPB7TEQ='
        os.environ['SMTP_RECEIVERS']='ArKBTrqPPMFtgjSYAl9EOeWksSBH0YiqSEb08oHVIKoFi0ZQA3euGwF2Ns98/BXV3GMEHjYOkVjlxIz6h0QjrmaPbjlkaPxV92SAgwP+Kn1w4SOJ1wrJLp+TvfOrIg6KkXyXmbZt2l+xcGo58vLIgyTiiL/p6ZfUjYF0uyLpHMM='

    def tearDown(self):
        '''
        测试之后的收尾
        如关闭数据库
        :return:
        '''
        pass

    def test01_sent_email(self):
        sender=Email_sender(package_key_res_path)
        sender.do_send('测试标题','测试文本体')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test01_sent_email'))
    runner = unittest.TextTestRunner()
    runner.run(suite)