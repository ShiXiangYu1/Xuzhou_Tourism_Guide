#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
路由模块
定义网站各页面的路由和视图函数
"""

from flask import Blueprint, render_template

# 创建蓝图
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """
    网站首页
    
    Returns:
        渲染后的首页模板
    """
    return render_template('index.html', title='徐州旅游攻略')


@main_bp.route('/food')
def food():
    """
    美食推荐页面
    
    Returns:
        渲染后的美食推荐页面模板
    """
    return render_template('food.html', title='徐州美食推荐')


@main_bp.route('/attractions')
def attractions():
    """
    景点推荐页面
    
    Returns:
        渲染后的景点推荐页面模板
    """
    return render_template('attractions.html', title='徐州景点推荐')


@main_bp.route('/itinerary')
def itinerary():
    """
    行程规划页面
    
    Returns:
        渲染后的行程规划页面模板
    """
    return render_template('itinerary.html', title='徐州行程规划')


@main_bp.route('/info')
def info():
    """
    实用信息页面
    
    Returns:
        渲染后的实用信息页面模板
    """
    return render_template('info.html', title='徐州实用信息') 