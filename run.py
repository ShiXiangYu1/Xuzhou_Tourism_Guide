#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
应用启动模块
用于启动Flask应用
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 