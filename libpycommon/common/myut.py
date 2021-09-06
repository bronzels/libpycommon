# coding:utf-8
import unittest
import os
# 用例路径
def all_case(path):
    case_path = os.path.join(os.getcwd(), path)
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test_*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

def entry(path):
    runner = unittest.TextTestRunner()
    runner.run(all_case(path))