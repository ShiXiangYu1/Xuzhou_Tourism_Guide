#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
地图导航集成测试
测试地图导航功能和链接生成是否正确
"""

import unittest
from flask import url_for
from app import create_app
from bs4 import BeautifulSoup


class MapIntegrationTest(unittest.TestCase):
    """地图导航功能集成测试"""

    def setUp(self):
        """测试前设置环境"""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)
        self.app.config['SERVER_NAME'] = 'localhost'
        self.app.config['WTF_CSRF_ENABLED'] = False

    def tearDown(self):
        """测试后清理环境"""
        self.app_context.pop()

    def test_food_page_has_navigation_buttons(self):
        """测试美食页面是否包含导航按钮"""
        response = self.client.get(url_for('food'))
        self.assertEqual(response.status_code, 200)
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.data, 'html.parser')
        
        # 检查导航按钮是否存在
        nav_buttons = soup.select('.map-nav-btn')
        self.assertTrue(len(nav_buttons) > 0, "导航按钮不存在")
        
        # 检查是否有带有坐标的按钮
        coords_buttons = [b for b in nav_buttons if b.get('data-lat') and b.get('data-lng')]
        self.assertTrue(len(coords_buttons) > 0, "没有带经纬度坐标的导航按钮")
        
        # 检查老玖烧烤的导航按钮是否有正确的坐标
        laojiu_buttons = [b for b in nav_buttons 
                         if b.get('data-name') and '老玖烧烤' in b.get('data-name')]
        if laojiu_buttons:
            laojiu_btn = laojiu_buttons[0]
            self.assertEqual(laojiu_btn.get('data-lat'), '34.2716', "老玖烧烤纬度坐标不正确")
            self.assertEqual(laojiu_btn.get('data-lng'), '117.1847', "老玖烧烤经度坐标不正确")

    def test_attractions_page_has_navigation_buttons(self):
        """测试景点页面是否包含导航按钮"""
        response = self.client.get(url_for('attractions'))
        self.assertEqual(response.status_code, 200)
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.data, 'html.parser')
        
        # 检查导航按钮是否存在
        nav_buttons = soup.select('.map-nav-btn')
        self.assertTrue(len(nav_buttons) > 0, "导航按钮不存在")
        
        # 检查云龙山风景区导航按钮是否有正确的坐标
        yunlong_buttons = [b for b in nav_buttons 
                          if b.get('data-name') and '云龙山' in b.get('data-name')]
        if yunlong_buttons:
            yunlong_btn = yunlong_buttons[0]
            self.assertEqual(yunlong_btn.get('data-lat'), '34.2732', "云龙山纬度坐标不正确")
            self.assertEqual(yunlong_btn.get('data-lng'), '117.2011', "云龙山经度坐标不正确")

    def test_navigation_script_is_included(self):
        """测试页面是否包含地图导航脚本"""
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        
        # 检查是否包含地图工具脚本
        self.assertIn(b'map-utils.js', response.data, "页面未包含地图工具脚本")
        
        # 检查是否包含地图导航样式
        self.assertIn(b'map-dropdown', response.data, "页面未包含地图导航样式")


if __name__ == '__main__':
    unittest.main() 