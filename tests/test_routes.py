#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
路由测试模块
用于测试Web应用的各个路由是否正常工作
"""

import unittest
from app import create_app
from flask import url_for


class TestRoutes(unittest.TestCase):
    """路由测试类"""

    def setUp(self):
        """测试前的准备工作"""
        self.app = create_app(testing=True)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """测试后的清理工作"""
        self.app_context.pop()

    def test_index_route(self):
        """测试首页路由"""
        response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州旅游攻略', response.data.decode('utf-8'))

    def test_food_route(self):
        """测试美食推荐路由"""
        response = self.client.get(url_for('main.food'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州美食推荐', response.data.decode('utf-8'))

    def test_local_food_route(self):
        """测试苍蝇馆子路由"""
        response = self.client.get(url_for('main.local_food'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州苍蝇馆子', response.data.decode('utf-8'))

    def test_attractions_route(self):
        """测试景点推荐路由"""
        response = self.client.get(url_for('main.attractions'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州景点推荐', response.data.decode('utf-8'))

    def test_hotspots_route(self):
        """测试网红打卡地路由"""
        response = self.client.get(url_for('main.hotspots'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州网红打卡地', response.data.decode('utf-8'))
        self.assertIn('网红打卡拍摄小贴士', response.data.decode('utf-8'))
        self.assertIn('云龙湖九里湾观景台', response.data.decode('utf-8'))

    def test_itinerary_route(self):
        """测试行程规划路由"""
        response = self.client.get(url_for('main.itinerary'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州行程规划', response.data.decode('utf-8'))

    def test_info_route(self):
        """测试实用信息路由"""
        response = self.client.get(url_for('main.info'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('徐州实用信息', response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main() 