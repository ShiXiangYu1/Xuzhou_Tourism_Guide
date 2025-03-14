#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
数据服务模块
提供数据访问功能，从模型中检索数据
"""

from app.models import FOOD_DATA, ATTRACTION_DATA, ITINERARY_DATA, PRACTICAL_INFO, LOCATION_COORDINATES


def get_all_foods():
    """
    获取所有美食项目
    
    Returns:
        list: 所有美食项目的列表
    """
    return [food.to_dict() for food in FOOD_DATA]


def get_local_food_spots():
    """
    获取当地特色小吃和苍蝇馆子
    
    Returns:
        list: 符合条件的当地小吃店列表
    """
    local_spots = [food.to_dict() for food in FOOD_DATA 
                  if food.name in ["小鱼卷饼", "老王地锅", "徐州凉皮"] 
                  or "特色小吃" in food.category]
    return local_spots


def get_food_by_category(category):
    """
    按类别获取美食项目
    
    Args:
        category: 美食类别
        
    Returns:
        list: 符合类别的美食项目列表
    """
    return [food.to_dict() for food in FOOD_DATA if food.category == category]


def get_all_attractions():
    """
    获取所有景点
    
    Returns:
        list: 所有景点的列表
    """
    return [attraction.to_dict() for attraction in ATTRACTION_DATA]


def get_attraction_by_category(category):
    """
    按类别获取景点
    
    Args:
        category: 景点类别
        
    Returns:
        list: 符合类别的景点列表
    """
    return [attraction.to_dict() for attraction in ATTRACTION_DATA 
            if attraction.category == category]


def get_itinerary():
    """
    获取行程规划
    
    Returns:
        list: 行程规划列表
    """
    return [itinerary.to_dict() for itinerary in ITINERARY_DATA]


def get_practical_info():
    """
    获取实用信息
    
    Returns:
        dict: 实用信息字典
    """
    return PRACTICAL_INFO


def filter_foods_by_rating(min_rating=0):
    """
    按评分筛选美食
    
    Args:
        min_rating: 最低评分，默认为0
        
    Returns:
        list: 符合评分条件的美食列表
    """
    return [food.to_dict() for food in FOOD_DATA if food.rating >= min_rating]


def filter_attractions_by_rating(min_rating=0):
    """
    按评分筛选景点
    
    Args:
        min_rating: 最低评分，默认为0
        
    Returns:
        list: 符合评分条件的景点列表
    """
    return [attraction.to_dict() for attraction in ATTRACTION_DATA 
            if attraction.rating >= min_rating]


def search_foods(keyword):
    """
    搜索美食
    
    Args:
        keyword: 搜索关键词
        
    Returns:
        list: 包含关键词的美食列表
    """
    if not keyword:
        return get_all_foods()
    
    keyword = keyword.lower()
    return [food.to_dict() for food in FOOD_DATA 
            if keyword in food.name.lower() or 
            keyword in food.description.lower() or
            keyword in food.category.lower()]


def search_attractions(keyword):
    """
    搜索景点
    
    Args:
        keyword: 搜索关键词
        
    Returns:
        list: 包含关键词的景点列表
    """
    if not keyword:
        return get_all_attractions()
    
    keyword = keyword.lower()
    return [attraction.to_dict() for attraction in ATTRACTION_DATA 
            if keyword in attraction.name.lower() or 
            keyword in attraction.description.lower() or
            keyword in attraction.category.lower()]


def get_featured_locations():
    """
    获取推荐的位置点
    
    Returns:
        dict: 包含推荐景点和美食的字典
    """
    featured_attractions = [a.to_dict() for a in ATTRACTION_DATA if a.featured]
    featured_foods = [f.to_dict() for f in FOOD_DATA if f.featured]
    
    return {
        'attractions': featured_attractions,
        'foods': featured_foods
    }


def get_all_map_coordinates():
    """
    获取所有地图坐标点
    
    Returns:
        list: 所有坐标点的列表
    """
    # 获取景点坐标
    attraction_coords = [
        {
            'name': a.name,
            'address': a.address,
            'lat': a.lat,
            'lng': a.lng,
            'category': a.category,
            'description': a.description,
            'type': 'attraction'
        }
        for a in ATTRACTION_DATA if a.lat and a.lng
    ]
    
    # 获取美食坐标
    food_coords = [
        {
            'name': f.name,
            'address': f.location,
            'lat': f.lat,
            'lng': f.lng,
            'category': f.category,
            'description': f.description,
            'type': 'food'
        }
        for f in FOOD_DATA if f.lat and f.lng
    ]
    
    # 获取其他坐标点
    other_coords = [loc.to_dict() for loc in LOCATION_COORDINATES]
    for loc in other_coords:
        loc['type'] = loc['category'].lower()
    
    # 合并所有坐标
    return attraction_coords + food_coords + other_coords


def get_coordinates_by_category(category):
    """
    按类别获取坐标点
    
    Args:
        category: 坐标点类别（如景点、美食、交通等）
        
    Returns:
        list: 符合类别的坐标点列表
    """
    all_coords = get_all_map_coordinates()
    if category.lower() == 'all':
        return all_coords
        
    return [coord for coord in all_coords 
            if category.lower() in coord['category'].lower() or 
               category.lower() in coord['type'].lower()]


def search_all_locations(keyword):
    """
    全局搜索所有位置
    
    Args:
        keyword: 搜索关键词
        
    Returns:
        dict: 分类搜索结果
    """
    if not keyword or len(keyword.strip()) < 2:
        return {'attractions': [], 'foods': [], 'others': []}
    
    keyword = keyword.lower().strip()
    
    # 搜索景点
    attractions = search_attractions(keyword)
    
    # 搜索美食
    foods = search_foods(keyword)
    
    # 搜索其他位置
    other_locations = [
        loc.to_dict() for loc in LOCATION_COORDINATES
        if (keyword in loc.name.lower() or 
            keyword in loc.address.lower() or 
            keyword in loc.description.lower() or
            keyword in loc.category.lower())
    ]
    
    return {
        'attractions': attractions, 
        'foods': foods, 
        'others': other_locations
    } 