#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
应用启动模块
用于启动Flask应用
"""

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=os.environ.get('DEBUG', 'True').lower() == 'true') 