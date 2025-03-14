#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Flask应用初始化模块
创建并配置Flask应用实例
"""

from flask import Flask


def create_app(config_name=None):
    """
    创建并返回Flask应用实例
    
    Args:
        config_name: 配置名称，用于加载不同环境的配置
        
    Returns:
        app: 配置好的Flask应用实例
    """
    # 创建Flask应用
    app = Flask(__name__)
    
    # 加载配置
    if config_name == 'testing':
        app.config['TESTING'] = True
    else:
        app.config['SECRET_KEY'] = 'xuzhou-travel-guide-key'
        app.config['DEBUG'] = True
    
    # 注册蓝图
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app 