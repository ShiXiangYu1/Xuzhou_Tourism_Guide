#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试运行文件
用于一次性运行所有测试
"""

import unittest
import os
import sys

# 添加项目根目录到 Python 模块搜索路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.tests.test_routes import RoutesTestCase
from app.tests.test_services import ServicesTestCase
from app.tests.test_models import ModelsTestCase


def run_tests():
    """运行所有测试"""
    # 创建测试套件
    test_suite = unittest.TestSuite()
    
    # 添加测试类
    test_suite.addTest(unittest.makeSuite(RoutesTestCase))
    test_suite.addTest(unittest.makeSuite(ServicesTestCase))
    test_suite.addTest(unittest.makeSuite(ModelsTestCase))
    
    # 运行测试
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(test_suite)
    
    # 返回结果，用于 CI/CD 集成
    return len(test_result.errors) == 0 and len(test_result.failures) == 0


if __name__ == '__main__':
    # 运行测试并设置退出码
    success = run_tests()
    sys.exit(0 if success else 1) 