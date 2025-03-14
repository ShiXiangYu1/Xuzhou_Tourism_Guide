#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试基类选择器
根据环境自动选择合适的测试基类
如果 flask_testing 可用，则使用它，否则使用替代版本
"""

import importlib.util

# 检查 flask_testing 是否可用
flask_testing_available = importlib.util.find_spec("flask_testing") is not None

try:
    if flask_testing_available:
        # 如果 flask_testing 可用，使用标准测试基类
        from app.tests.test_base import BaseTestCase
        print("使用标准测试基类（基于 flask_testing）")
    else:
        # 否则使用替代测试基类
        from app.tests.test_base_alt import BaseTestCaseAlt as BaseTestCase
        print("使用替代测试基类（不依赖 flask_testing）")
except ImportError as e:
    # 出现任何导入错误，回退到替代测试基类
    from app.tests.test_base_alt import BaseTestCaseAlt as BaseTestCase
    print(f"导入错误，回退到替代测试基类: {e}")

# 导出选择的测试基类
__all__ = ['BaseTestCase'] 