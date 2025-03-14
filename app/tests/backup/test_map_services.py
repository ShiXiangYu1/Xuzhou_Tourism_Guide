#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
地图服务测试模块
测试地图和坐标相关的服务函数是否正确工作
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
    get_all_map_coordinates, get_coordinates_by_category, 
    get_featured_locations, search_all_locations
)


class MapServicesTestCase(BaseTestCase):
    """地图服务测试类"""
    
    def test_get_all_map_coordinates(self):
        """测试获取所有地图坐标点"""
        coordinates = get_all_map_coordinates()
        
        # 验证返回值类型和非空
        self.assertIsInstance(coordinates, list)
        self.assertGreater(len(coordinates), 0)
        
        # 验证每个坐标点包含必要的属性
        for coord in coordinates:
            self.assertIn('name', coord)
            self.assertIn('address', coord)
            self.assertIn('lat', coord)
            self.assertIn('lng', coord)
            self.assertIn('type', coord)
            
            # 验证经纬度是数值类型
            self.assertIsInstance(coord['lat'], (int, float))
            self.assertIsInstance(coord['lng'], (int, float))
    
    def test_get_coordinates_by_category(self):
        """测试按类别获取坐标点"""
        # 测试景点类别
        attraction_coords = get_coordinates_by_category('attraction')
        self.assertIsInstance(attraction_coords, list)
        self.assertGreater(len(attraction_coords), 0)
        for coord in attraction_coords:
            self.assertEqual(coord['type'], 'attraction')
        
        # 测试美食类别
        food_coords = get_coordinates_by_category('food')
        self.assertIsInstance(food_coords, list)
        self.assertGreater(len(food_coords), 0)
        for coord in food_coords:
            self.assertEqual(coord['type'], 'food')
        
        # 测试其他类别 - 交通
        traffic_coords = get_coordinates_by_category('交通')
        self.assertIsInstance(traffic_coords, list)
        for coord in traffic_coords:
            self.assertTrue(
                coord['category'].lower() == '交通' or
                coord['type'].lower() == 'traffic'
            )
            
        # 测试获取所有坐标
        all_coords = get_coordinates_by_category('all')
        self.assertEqual(len(all_coords), len(get_all_map_coordinates()))
    
    def test_get_featured_locations(self):
        """测试获取推荐的位置点"""
        featured = get_featured_locations()
        
        # 验证返回值结构
        self.assertIsInstance(featured, dict)
        self.assertIn('attractions', featured)
        self.assertIn('foods', featured)
        
        # 验证推荐景点
        self.assertIsInstance(featured['attractions'], list)
        for attraction in featured['attractions']:
            self.assertTrue(attraction['featured'])
            
        # 验证推荐美食
        self.assertIsInstance(featured['foods'], list)
        for food in featured['foods']:
            self.assertTrue(food['featured'])
    
    def test_search_all_locations(self):
        """测试全局搜索所有位置"""
        # 测试有效关键词搜索
        results = search_all_locations('云龙')
        self.assertIsInstance(results, dict)
        self.assertIn('attractions', results)
        self.assertIn('foods', results)
        self.assertIn('others', results)
        
        # 判断是否至少有一个结果
        has_results = bool(results['attractions']) or bool(results['foods']) or bool(results['others'])
        self.assertTrue(has_results)
        
        # 测试无效关键词搜索
        invalid_results = search_all_locations('zzzzzzz')
        self.assertFalse(bool(invalid_results['attractions']))
        self.assertFalse(bool(invalid_results['foods']))
        self.assertFalse(bool(invalid_results['others']))
        
        # 测试空关键词
        empty_results = search_all_locations('')
        self.assertFalse(bool(empty_results['attractions']))
        self.assertFalse(bool(empty_results['foods']))
        self.assertFalse(bool(empty_results['others']))
        
        # 测试关键词过短
        short_results = search_all_locations('a')
        self.assertFalse(bool(short_results['attractions']))
        self.assertFalse(bool(short_results['foods']))
        self.assertFalse(bool(short_results['others']))


if __name__ == '__main__':
    unittest.main() 