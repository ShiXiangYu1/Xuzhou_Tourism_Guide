#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试覆盖率运行脚本
用于运行测试并生成覆盖率报告
"""

import os
import sys
import coverage
import unittest

# 添加项目根目录到 Python 模块搜索路径
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def run_tests_with_coverage():
    """运行测试并生成覆盖率报告"""
    # 创建覆盖率对象
    cov = coverage.Coverage(config_file="app/tests/.coveragerc")
    
    # 启动覆盖率测量
    cov.start()
    
    # 导入测试模块
    from app.tests.test_routes import RoutesTestCase
    from app.tests.test_services import ServicesTestCase
    from app.tests.test_models import ModelsTestCase
    
    # 创建测试套件
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(RoutesTestCase))
    test_suite.addTest(unittest.makeSuite(ServicesTestCase))
    test_suite.addTest(unittest.makeSuite(ModelsTestCase))
    
    # 运行测试
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(test_suite)
    
    # 停止覆盖率测量
    cov.stop()
    
    # 保存覆盖率数据
    cov.save()
    
    # 打印覆盖率报告
    print("\n覆盖率报告:")
    cov.report()
    
    # 生成HTML覆盖率报告
    cov.html_report()
    
    print("\nHTML覆盖率报告已生成到 coverage_html_report 目录")
    
    # 返回测试结果
    return len(test_result.errors) == 0 and len(test_result.failures) == 0


if __name__ == "__main__":
    # 运行测试并设置退出码
    success = run_tests_with_coverage()
    sys.exit(0 if success else 1) 