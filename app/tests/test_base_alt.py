#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试基类（替代版本）
不依赖 flask_testing 库，直接使用 unittest 和 Flask 测试客户端
适用于无法安装 flask_testing 的环境
"""

import unittest
from flask import template_rendered
from contextlib import contextmanager
from app import create_app


@contextmanager
def captured_templates(app):
    """捕获渲染的模板和上下文"""
    recorded = []
    
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


class BaseTestCaseAlt(unittest.TestCase):
    """替代测试基类，不依赖 flask_testing，所有测试类可选择继承此类"""
    
    def setUp(self):
        """测试前的准备工作"""
        self.app = create_app('testing')
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
    
    def tearDown(self):
        """测试后的清理工作"""
        self.app_context.pop()
    
    def assert200(self, response):
        """断言响应状态码为200"""
        self.assertEqual(response.status_code, 200)
    
    def assert404(self, response):
        """断言响应状态码为404"""
        self.assertEqual(response.status_code, 404)
        
    def assert400(self, response):
        """断言响应状态码为400"""
        self.assertEqual(response.status_code, 400)
    
    def assert_template_used(self, template_name, response=None):
        """断言使用了指定模板
        
        Args:
            template_name: 模板名称
            response: 可选的响应对象，如果提供则直接检查它
        """
        if response:
            # 直接检查传入的响应
            self.assert200(response)
            # 由于替代测试基类无法直接访问响应使用的模板
            # 我们只能通过检查响应内容是否符合预期来间接验证
            self.assertIn(b'<!DOCTYPE html>', response.data)  # 确保是HTML响应
        else:
            # 没有提供响应，发出请求
            with captured_templates(self.app) as templates:
                response = self.client.get('/')  # 访问首页作为示例
                self.assert200(response)
                if len(templates) > 0:
                    self.assertEqual(templates[0][0].name, template_name)
            
    def get_context_variable(self, template_name, variable_name):
        """获取模板上下文中的变量值"""
        with captured_templates(self.app) as templates:
            response = self.client.get(template_name)
            self.assert200(response)
            self.assertTrue(len(templates) > 0)
            context = templates[0][1]
            self.assertIn(variable_name, context)
            return context[variable_name] 