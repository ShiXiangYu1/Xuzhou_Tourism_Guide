#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
路由测试模块
测试所有页面路由是否正常工作
"""

import unittest
import importlib.util

# 尝试导入标准测试基类，如果失败则使用替代测试基类
try:
    # 检查 flask_testing 是否可用
    flask_testing_available = importlib.util.find_spec("flask_testing") is not None
    
    if flask_testing_available:
        from app.tests.test_base import BaseTestCase
    else:
        # 使用替代测试基类
        from app.tests.test_base_alt import BaseTestCaseAlt as BaseTestCase
        print("注意: 使用替代测试基类 BaseTestCaseAlt")
except ImportError as e:
    # 导入失败时使用替代测试基类
    from app.tests.test_base_alt import BaseTestCaseAlt as BaseTestCase
    print(f"导入错误，使用替代测试基类: {e}")
class RoutesTestCase(BaseTestCase):
    """路由测试类"""
    
    def test_home_page(self):
        """测试首页路由"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州旅游攻略', response.data.decode('utf-8'))
        self.assertIn('寻味大汉风情之都', response.data.decode('utf-8'))
    
    def test_food_page(self):
        """测试美食推荐页面路由"""
        response = self.client.get('/food')
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州美食推荐', response.data.decode('utf-8'))
        self.assertIn('老玖烧烤', response.data.decode('utf-8'))
    
    def test_attractions_page(self):
        """测试景点推荐页面路由"""
        response = self.client.get('/attractions')
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州景点推荐', response.data.decode('utf-8'))
        self.assertIn('云龙山风景区', response.data.decode('utf-8'))
    
    def test_itinerary_page(self):
        """测试行程规划页面路由"""
        response = self.client.get('/itinerary')
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州行程规划', response.data.decode('utf-8'))
    
    def test_info_page(self):
        """测试实用信息页面路由"""
        response = self.client.get('/info')
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州实用信息', response.data.decode('utf-8'))
    
    def test_non_existent_page(self):
        """测试访问不存在的页面是否返回404"""
        response = self.client.get('/non-existent-page')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main() 