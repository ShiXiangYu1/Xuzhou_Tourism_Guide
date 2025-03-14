#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试基类
提供测试所需的基本设置
"""

from flask_testing import TestCase
from app import create_app


class BaseTestCase(TestCase):
    """测试基类，所有测试类都应继承此类"""
    
    def create_app(self):
        """创建并配置用于测试的Flask应用实例"""
        app = create_app('testing')
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    def setUp(self):
        """测试前的准备工作"""
        pass
    
    def tearDown(self):
        """测试后的清理工作"""
        pass 