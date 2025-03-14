#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
服务测试模块
测试数据服务函数是否正确工作
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
from app.services import (
    get_all_foods, get_food_by_category, get_all_attractions, 
    get_attraction_by_category, get_itinerary, get_practical_info,
    filter_foods_by_rating, filter_attractions_by_rating,
    search_foods, search_attractions
)


class ServicesTestCase(BaseTestCase):
    """服务测试类"""
    
    def test_get_all_foods(self):
        """测试获取所有美食项目"""
        foods = get_all_foods()
        self.assertIsInstance(foods, list)
        self.assertGreater(len(foods), 0)
        self.assertIn('name', foods[0])
        self.assertIn('category', foods[0])
        self.assertIn('location', foods[0])
    
    def test_get_food_by_category(self):
        """测试按类别获取美食项目"""
        category = "烧烤"
        foods = get_food_by_category(category)
        self.assertIsInstance(foods, list)
        self.assertGreater(len(foods), 0)
        for food in foods:
            self.assertEqual(food['category'], category)
    
    def test_get_all_attractions(self):
        """测试获取所有景点"""
        attractions = get_all_attractions()
        self.assertIsInstance(attractions, list)
        self.assertGreater(len(attractions), 0)
        self.assertIn('name', attractions[0])
        self.assertIn('category', attractions[0])
        self.assertIn('address', attractions[0])
    
    def test_get_attraction_by_category(self):
        """测试按类别获取景点"""
        category = "历史文化类"
        attractions = get_attraction_by_category(category)
        self.assertIsInstance(attractions, list)
        self.assertGreater(len(attractions), 0)
        for attraction in attractions:
            self.assertEqual(attraction['category'], category)
    
    def test_get_itinerary(self):
        """测试获取行程规划"""
        itinerary = get_itinerary()
        self.assertIsInstance(itinerary, list)
        self.assertGreater(len(itinerary), 0)
        self.assertIn('day', itinerary[0])
        self.assertIn('morning_plan', itinerary[0])
        self.assertIn('lunch_plan', itinerary[0])
    
    def test_get_practical_info(self):
        """测试获取实用信息"""
        info = get_practical_info()
        self.assertIsInstance(info, dict)
        self.assertIn('transportation', info)
        self.assertIn('accommodation', info)
        self.assertIn('season', info)
        self.assertIn('tips', info)
    
    def test_filter_foods_by_rating(self):
        """测试按评分筛选美食"""
        min_rating = 4.5
        foods = filter_foods_by_rating(min_rating)
        self.assertIsInstance(foods, list)
        for food in foods:
            self.assertGreaterEqual(food['rating'], min_rating)
    
    def test_filter_attractions_by_rating(self):
        """测试按评分筛选景点"""
        min_rating = 4.7
        attractions = filter_attractions_by_rating(min_rating)
        self.assertIsInstance(attractions, list)
        for attraction in attractions:
            self.assertGreaterEqual(attraction['rating'], min_rating)
    
    def test_search_foods(self):
        """测试搜索美食"""
        keyword = "烧烤"
        foods = search_foods(keyword)
        self.assertIsInstance(foods, list)
        self.assertGreater(len(foods), 0)
        
        # 测试空关键词应该返回所有美食
        all_foods = search_foods("")
        self.assertEqual(len(all_foods), len(get_all_foods()))
    
    def test_search_attractions(self):
        """测试搜索景点"""
        keyword = "博物馆"
        attractions = search_attractions(keyword)
        self.assertIsInstance(attractions, list)
        self.assertGreater(len(attractions), 0)
        
        # 测试空关键词应该返回所有景点
        all_attractions = search_attractions("")
        self.assertEqual(len(all_attractions), len(get_all_attractions()))


if __name__ == '__main__':
    unittest.main() 