#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
路由模块
定义网站各页面的路由和视图函数
"""

from flask import Blueprint, render_template, jsonify, request, abort

from app.services import (
    get_all_foods, get_all_attractions, get_itinerary, get_practical_info,
    get_local_food_spots, get_all_map_coordinates, get_coordinates_by_category,
    get_featured_locations, search_all_locations
)

# 创建蓝图
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """
    网站首页
    
    Returns:
        渲染后的首页模板
    """
    featured = get_featured_locations()
    return render_template('index.html', title='徐州旅游攻略', featured=featured)


@main_bp.route('/food')
def food():
    """
    美食推荐页面
    
    Returns:
        渲染后的美食推荐页面模板
    """
    foods = get_all_foods()
    return render_template('food.html', title='徐州美食推荐', foods=foods)


@main_bp.route('/local_food')
def local_food():
    """
    苍蝇馆子 - 地道美食页面
    
    Returns:
        渲染后的地道美食页面模板
    """
    local_foods = get_local_food_spots()
    return render_template('local_food.html', title='徐州苍蝇馆子 - 地道美食', local_foods=local_foods)


@main_bp.route('/attractions')
def attractions():
    """
    景点推荐页面
    
    Returns:
        渲染后的景点推荐页面模板
    """
    all_attractions = get_all_attractions()
    return render_template('attractions.html', title='徐州景点推荐', attractions=all_attractions)


@main_bp.route('/itinerary')
def itinerary():
    """
    行程规划页面
    
    Returns:
        渲染后的行程规划页面模板
    """
    itinerary_data = get_itinerary()
    return render_template('itinerary.html', title='徐州行程规划', itinerary=itinerary_data)


@main_bp.route('/info')
def info():
    """
    实用信息页面
    
    Returns:
        渲染后的实用信息页面模板
    """
    practical_info = get_practical_info()
    return render_template('info.html', title='徐州实用信息', info=practical_info)


@main_bp.route('/hotspots')
def hotspots():
    """
    网红打卡地页面
    
    Returns:
        渲染后的网红打卡地页面模板
    """
    return render_template('hotspots.html', title='徐州网红打卡地')


@main_bp.route('/map')
def tourist_map():
    """
    徐州旅游地图整合页面
    
    Returns:
        渲染后的旅游地图页面模板
    """
    return render_template('map.html', title='徐州旅游地图')


@main_bp.route('/search')
def search():
    """
    搜索页面
    
    Returns:
        渲染后的搜索结果页面模板
    """
    query = request.args.get('q', '')
    search_results = search_all_locations(query) if query else {}
    return render_template('search.html', title='搜索结果', 
                           query=query, results=search_results)


# API 端点
@main_bp.route('/api/coordinates')
def get_coordinates():
    """
    获取地图坐标点API端点
    
    Returns:
        JSON: 所有坐标点数据
    """
    category = request.args.get('category', 'all')
    coordinates = get_coordinates_by_category(category)
    return jsonify(coordinates)


@main_bp.route('/api/search')
def api_search():
    """
    搜索API端点
    
    Returns:
        JSON: 搜索结果
    """
    query = request.args.get('q', '')
    if not query or len(query.strip()) < 2:
        return jsonify({"error": "搜索关键词太短，请输入至少2个字符"}), 400
    
    results = search_all_locations(query)
    return jsonify(results) 