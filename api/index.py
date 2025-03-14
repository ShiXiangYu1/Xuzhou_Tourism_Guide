"""
Vercel部署入口文件
该文件是Vercel部署时的入口点
"""

from flask import Flask
from app import create_app

# 创建应用实例
app = create_app()

# Vercel需要的变量名
index = app

# 这是 Vercel 需要的入口点
app.debug = False

if __name__ == '__main__':
    app.run() 