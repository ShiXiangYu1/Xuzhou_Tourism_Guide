#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
模型测试模块
测试数据模型类是否正确实现
"""

import unittest
from app.tests.test_base import BaseTestCase
from app.models import FoodItem, Attraction, Itinerary


class ModelsTestCase(BaseTestCase):
    """模型测试类"""
    
    def test_food_item_init(self):
        """测试美食项目类初始化"""
        food = FoodItem(
            name="测试美食",
            category="测试类别",
            location="测试位置",
            description="测试描述",
            rating=4.5,
            image="test.jpg"
        )
        
        self.assertEqual(food.name, "测试美食")
        self.assertEqual(food.category, "测试类别")
        self.assertEqual(food.location, "测试位置")
        self.assertEqual(food.description, "测试描述")
        self.assertEqual(food.rating, 4.5)
        self.assertEqual(food.image, "test.jpg")
    
    def test_food_item_to_dict(self):
        """测试美食项目转换为字典"""
        food = FoodItem(
            name="测试美食",
            category="测试类别",
            location="测试位置",
            description="测试描述",
            rating=4.5,
            image="test.jpg"
        )
        
        food_dict = food.to_dict()
        self.assertIsInstance(food_dict, dict)
        self.assertEqual(food_dict['name'], "测试美食")
        self.assertEqual(food_dict['category'], "测试类别")
        self.assertEqual(food_dict['location'], "测试位置")
        self.assertEqual(food_dict['description'], "测试描述")
        self.assertEqual(food_dict['rating'], 4.5)
        self.assertEqual(food_dict['image'], "test.jpg")
    
    def test_food_item_default_image(self):
        """测试美食项目默认图片"""
        food = FoodItem(
            name="测试美食",
            category="测试类别",
            location="测试位置",
            description="测试描述",
            rating=4.5
        )
        
        self.assertEqual(food.image, "default_food.jpg")
    
    def test_attraction_init(self):
        """测试景点类初始化"""
        attraction = Attraction(
            name="测试景点",
            category="测试类别",
            address="测试地址",
            description="测试描述",
            rating=4.8,
            opening_hours="9:00-17:00",
            ticket_price="50元",
            image="test.jpg"
        )
        
        self.assertEqual(attraction.name, "测试景点")
        self.assertEqual(attraction.category, "测试类别")
        self.assertEqual(attraction.address, "测试地址")
        self.assertEqual(attraction.description, "测试描述")
        self.assertEqual(attraction.rating, 4.8)
        self.assertEqual(attraction.opening_hours, "9:00-17:00")
        self.assertEqual(attraction.ticket_price, "50元")
        self.assertEqual(attraction.image, "test.jpg")
    
    def test_attraction_to_dict(self):
        """测试景点转换为字典"""
        attraction = Attraction(
            name="测试景点",
            category="测试类别",
            address="测试地址",
            description="测试描述",
            rating=4.8,
            opening_hours="9:00-17:00",
            ticket_price="50元",
            image="test.jpg"
        )
        
        attraction_dict = attraction.to_dict()
        self.assertIsInstance(attraction_dict, dict)
        self.assertEqual(attraction_dict['name'], "测试景点")
        self.assertEqual(attraction_dict['category'], "测试类别")
        self.assertEqual(attraction_dict['address'], "测试地址")
        self.assertEqual(attraction_dict['description'], "测试描述")
        self.assertEqual(attraction_dict['rating'], 4.8)
        self.assertEqual(attraction_dict['opening_hours'], "9:00-17:00")
        self.assertEqual(attraction_dict['ticket_price'], "50元")
        self.assertEqual(attraction_dict['image'], "test.jpg")
    
    def test_attraction_default_image(self):
        """测试景点默认图片"""
        attraction = Attraction(
            name="测试景点",
            category="测试类别",
            address="测试地址",
            description="测试描述",
            rating=4.8
        )
        
        self.assertEqual(attraction.image, "default_attraction.jpg")
    
    def test_itinerary_init(self):
        """测试行程类初始化"""
        itinerary = Itinerary(
            day=1,
            morning_plan="早上计划",
            lunch_plan="午餐计划",
            afternoon_plan="下午计划",
            dinner_plan="晚餐计划"
        )
        
        self.assertEqual(itinerary.day, 1)
        self.assertEqual(itinerary.morning_plan, "早上计划")
        self.assertEqual(itinerary.lunch_plan, "午餐计划")
        self.assertEqual(itinerary.afternoon_plan, "下午计划")
        self.assertEqual(itinerary.dinner_plan, "晚餐计划")
    
    def test_itinerary_to_dict(self):
        """测试行程转换为字典"""
        itinerary = Itinerary(
            day=1,
            morning_plan="早上计划",
            lunch_plan="午餐计划",
            afternoon_plan="下午计划",
            dinner_plan="晚餐计划"
        )
        
        itinerary_dict = itinerary.to_dict()
        self.assertIsInstance(itinerary_dict, dict)
        self.assertEqual(itinerary_dict['day'], 1)
        self.assertEqual(itinerary_dict['morning_plan'], "早上计划")
        self.assertEqual(itinerary_dict['lunch_plan'], "午餐计划")
        self.assertEqual(itinerary_dict['afternoon_plan'], "下午计划")
        self.assertEqual(itinerary_dict['dinner_plan'], "晚餐计划")


if __name__ == '__main__':
    unittest.main() 