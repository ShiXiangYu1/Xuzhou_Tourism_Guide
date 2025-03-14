#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
地图路由测试模块
测试地图和搜索相关的路由是否正确工作
"""

import json
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
class MapRoutesTestCase(BaseTestCase):
    """地图路由测试类"""
    
    def test_tourist_map_page(self):
        """测试徐州旅游地图页面"""
        response = self.client.get('/map')
        
        # 验证状态码和内容类型
        self.assert200(response)
        self.assert_template_used('map.html', response)
        
        # 验证页面标题和关键元素
        self.assertIn('徐州旅游地图'.encode('utf-8'), response.data)
        self.assertIn(b'id="map-container"', response.data)
        self.assertIn(b'id="location-type"', response.data)
    
    def test_search_page_no_query(self):
        """测试搜索页面 - 无查询参数"""
        response = self.client.get('/search')
        
        # 验证状态码和模板
        self.assert200(response)
        self.assert_template_used('search.html', response)
        
        # 验证显示搜索提示
        self.assertIn('请输入搜索关键词'.encode('utf-8'), response.data)
    
    def test_search_page_with_query(self):
        """测试搜索页面 - 有查询参数"""
        response = self.client.get('/search?q=云龙')
        
        # 验证状态码和模板
        self.assert200(response)
        self.assert_template_used('search.html', response)
        
        # 搜索结果应包含关键词
        self.assertIn('云龙'.encode('utf-8'), response.data)
    
    def test_search_page_no_results(self):
        """测试搜索页面 - 无搜索结果"""
        response = self.client.get('/search?q=zzzzzzzzz')
        
        # 验证状态码和模板
        self.assert200(response)
        self.assert_template_used('search.html', response)
        
        # 应显示无结果提示
        self.assertIn('未找到'.encode('utf-8'), response.data)
        self.assertIn('热门推荐'.encode('utf-8'), response.data)
    
    def test_coordinates_api(self):
        """测试获取坐标点API端点"""
        response = self.client.get('/api/coordinates')
        
        # 验证状态码和内容类型
        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')
        
        # 解析JSON响应
        data = json.loads(response.data)
        
        # 验证数据结构
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        
        # 验证每个坐标点包含必要的属性
        for coord in data:
            self.assertIn('name', coord)
            self.assertIn('address', coord)
            self.assertIn('lat', coord)
            self.assertIn('lng', coord)
    
    def test_coordinates_api_with_category(self):
        """测试按类别获取坐标点API端点"""
        response = self.client.get('/api/coordinates?category=attraction')
        
        # 验证状态码和内容类型
        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')
        
        # 解析JSON响应
        data = json.loads(response.data)
        
        # 验证数据结构
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        
        # 验证返回的都是景点类型
        for coord in data:
            self.assertEqual(coord['type'], 'attraction')
    
    def test_search_api_empty_query(self):
        """测试搜索API - 空查询参数"""
        response = self.client.get('/api/search')
        
        # 验证状态码和内容类型
        self.assert400(response)
        self.assertEqual(response.content_type, 'application/json')
        
        # 解析JSON响应
        data = json.loads(response.data)
        
        # 验证错误消息
        self.assertIn('error', data)
    
    def test_search_api_valid_query(self):
        """测试搜索API - 有效查询参数"""
        response = self.client.get('/api/search?q=云龙')
        
        # 验证状态码和内容类型
        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')
        
        # 解析JSON响应
        data = json.loads(response.data)
        
        # 验证数据结构
        self.assertIn('attractions', data)
        self.assertIn('foods', data)
        self.assertIn('others', data)
        
        # 验证至少有一个结果
        has_results = bool(data['attractions']) or bool(data['foods']) or bool(data['others'])
        self.assertTrue(has_results)
    
    def test_search_api_invalid_query(self):
        """测试搜索API - 无效查询参数"""
        response = self.client.get('/api/search?q=zz')
        
        # 验证状态码和内容类型
        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')
        
        # 解析JSON响应
        data = json.loads(response.data)
        
        # 验证数据结构
        self.assertIn('attractions', data)
        self.assertIn('foods', data)
        self.assertIn('others', data)
        
        # 验证没有结果
        self.assertEqual(len(data['attractions']), 0)
        self.assertEqual(len(data['foods']), 0)
        self.assertEqual(len(data['others']), 0)


if __name__ == '__main__':
    unittest.main() 