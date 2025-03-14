# 徐州旅游攻略网站

一个用于展示徐州旅游攻略的网站，特别关注美食推荐和景点介绍。

## 项目结构

```
旅游攻略/
├── app/                    # 应用主目录
│   ├── static/             # 静态文件
│   │   ├── css/            # CSS样式文件
│   │   ├── js/             # JavaScript文件
│   │   ├── img/            # 图片资源
│   ├── templates/          # HTML模板
│   ├── tests/              # 单元测试
├── requirements.txt        # 项目依赖
├── run.py                  # 应用启动文件
├── run_tests_with_coverage.py # 测试覆盖率运行脚本
```

## 开发进度

- [x] 创建项目基本结构
- [x] 实现首页布局
- [x] 实现美食推荐页面
- [x] 实现景点推荐页面
- [x] 实现行程规划页面
- [x] 实现实用信息页面
- [x] 完成单元测试
- [ ] 完成代码审核

## 功能特性

- 响应式设计，适配各种设备
- 美食推荐页面，展示徐州特色美食
- 景点推荐页面，介绍徐州主要景点
- 行程规划页面，提供多天游览计划
- 实用信息页面，提供交通、住宿等信息
- 完整的单元测试和测试覆盖率分析

## 如何运行

1. 安装依赖：`pip install -r requirements.txt`
2. 运行应用：`python run.py`
3. 访问网站：`http://localhost:5000`

## 如何运行测试

1. 运行所有测试：`python -m app.tests.run_tests`
2. 运行测试覆盖率分析：`python run_tests_with_coverage.py`

## 技术栈

- 后端：Python Flask
- 前端：HTML, CSS, JavaScript, Bootstrap 5
- 测试：Pytest, pytest-cov 