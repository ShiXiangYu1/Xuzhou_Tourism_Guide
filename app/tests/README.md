# 徐州旅游攻略网站测试文档

本文档描述了徐州旅游攻略网站的测试结构和运行方法。

## 后端测试

后端测试使用Python的`unittest`框架，测试文件位于`app/tests`目录下。

### 测试文件结构

- `test_base.py`: 测试基础类，提供Flask应用测试环境（依赖flask_testing）
- `test_base_alt.py`: 替代测试基类，不依赖flask_testing库
- `test_base_selector.py`: 测试基类选择器，根据环境自动选择适当的测试基类
- `test_models.py`: 测试数据模型，包括美食项目、景点、行程和位置坐标
- `test_services.py`: 测试数据服务层功能
- `test_routes.py`: 测试基础路由功能
- `test_map_services.py`: 测试地图和坐标服务功能
- `test_map_routes.py`: 测试地图和搜索路由功能

### 运行测试

**方法一：使用灵活的测试运行脚本（推荐）**

```bash
python run_tests_flexible.py
```

这个脚本会自动检查环境依赖情况，并选择合适的方式运行测试。

**方法二：标准方式运行测试**

```bash
# 安装依赖
pip install flask_testing

# 使用unittest运行测试
python -m unittest discover app.tests

# 或使用提供的测试脚本（包含覆盖率报告）
python run_tests_with_coverage.py
```

## 依赖问题解决方案

如果你在运行测试时遇到依赖安装问题，可以尝试以下解决方案：

### 1. 使用替代安装命令

```bash
# 临时关闭SSL验证
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org flask_testing

# 或使用国内镜像源
pip install -i https://mirrors.aliyun.com/pypi/simple/ flask_testing
```

### 2. 离线安装方法

```bash
# 在有网络的环境下下载依赖包
pip download -d ./deps flask-testing==0.8.1 coverage==7.3.2

# 将deps文件夹复制到目标环境

# 在目标环境中安装
pip install --no-index --find-links=./deps flask-testing coverage
```

### 3. 使用不依赖flask_testing的测试方法

如果确实无法安装依赖，可以使用替代测试基类运行测试：

```bash
# 修改测试代码中的导入语句
# 将 `from app.tests.test_base import BaseTestCase`
# 改为 `from app.tests.test_base_selector import BaseTestCase`

# 然后正常运行测试
python -m unittest discover app.tests
```

## 前端测试

前端JavaScript测试使用Mocha和Chai框架，测试文件位于`app/static/js/tests`目录下。

### 测试文件结构

- `test-map-utils.js`: 测试地图工具函数
- `test-runner.html`: 在浏览器中运行测试的HTML文件

### 运行测试

1. 启动Flask应用：
   ```bash
   python run.py
   ```

2. 在浏览器中打开测试运行器：
   ```
   http://localhost:5000/static/js/tests/test-runner.html
   ```

## 测试覆盖范围

当前测试覆盖了以下功能：

1. **数据模型**
   - `FoodItem`: 美食项目类
   - `Attraction`: 景点类
   - `Itinerary`: 行程类
   - `LocationCoordinates`: 位置坐标类

2. **服务函数**
   - 美食和景点数据检索和筛选
   - 地图坐标获取和分类
   - 搜索功能

3. **路由功能**
   - 基本页面路由
   - 地图和搜索相关路由
   - API端点

4. **JavaScript功能**
   - 地图导航工具函数
   - 多地图服务支持
   - 用户界面交互

## 测试注意事项

1. 运行测试前确保已安装所有依赖库，或使用替代测试基类
2. 前端测试需要网络连接以加载CDN资源 (Mocha和Chai)
3. 对百度地图API的测试可能需要有效的API密钥
4. 如果遇到ImportError或ModuleNotFoundError，请检查依赖安装情况 