# 徐州旅游攻略网站

[![Vercel部署状态](https://img.shields.io/badge/Vercel-已部署-success)](https://xuzhou-tourism-guide.vercel.app/)

一个用于展示徐州旅游攻略的网站，特别关注美食推荐、景点介绍、地图导航和搜索功能。

## 项目结构

```
旅游攻略/
├── app/                    # 应用主目录
│   ├── static/             # 静态文件
│   │   ├── css/            # CSS样式文件
│   │   ├── js/             # JavaScript文件
│   │   │   ├── tests/      # JavaScript测试文件
│   │   ├── img/            # 图片资源
│   │   ├── templates/      # HTML模板
│   │   │   ├── macros/     # 模板宏
│   │   ├── tests/          # 单元测试
│   ├── api/                # Vercel部署目录
│   │   ├── index.py        # Vercel入口文件
│   ├── requirements.txt    # 项目依赖
│   ├── run.py              # 应用启动文件
│   ├── run_tests_with_coverage.py # 测试覆盖率运行脚本
│   ├── vercel.json         # Vercel配置文件
```

## 开发进度

- [x] 创建项目基本结构
- [x] 实现首页布局
- [x] 实现美食推荐页面
- [x] 实现景点推荐页面
- [x] 实现行程规划页面
- [x] 实现实用信息页面
- [x] 实现地图导航功能
- [x] 实现全站搜索功能
- [x] 优化移动端体验
- [x] 完成后端单元测试
- [x] 完成前端JavaScript测试
- [x] 完成代码审核
- [ ] 部署到Vercel

## 功能特性

- 响应式设计，适配各种设备
- 美食推荐页面，展示徐州特色美食
- 景点推荐页面，介绍徐州主要景点
- 行程规划页面，提供多天游览计划
- 实用信息页面，提供交通、住宿等信息
- 网红打卡地页面，整合小红书和抖音热门内容
- **旅游地图**，集成多种位置类型，支持筛选和搜索
- **多种地图导航**，支持百度、高德、腾讯、Apple和Google地图
- **全站搜索功能**，可快速定位景点、美食和其他位置
- **完善的移动端优化**，提供流畅的手机浏览体验
- 完整的后端单元测试和前端JavaScript测试

## 如何运行

1. 安装依赖：`pip install -r requirements.txt`
2. 运行应用：`python run.py`
3. 访问网站：`http://localhost:5000`

## 如何运行测试

### 后端测试
1. 安装测试依赖：`pip install flask_testing`
2. 运行所有测试：`python -m unittest discover app.tests`
3. 运行测试覆盖率分析：`python run_tests_with_coverage.py`

### 前端测试
1. 启动服务器：`python run.py`
2. 在浏览器中访问：`http://localhost:5000/static/js/tests/test-runner.html`

更多测试说明，请参考 [测试文档](app/tests/README.md)。

## 如何部署到Vercel

项目已配置好Vercel部署所需的文件和设置。详细的部署指南请参考[DEPLOY.md](DEPLOY.md)文档。

简要步骤：

1. 将代码推送到GitHub仓库
2. 在Vercel中导入该仓库
3. 配置必要的环境变量：
   - `SECRET_KEY`: 应用密钥
   - `VERCEL_ENV`: `production`
4. 点击部署

也可以使用Vercel CLI进行部署：

```bash
# 安装Vercel CLI
npm i -g vercel

# 登录
vercel login

# 部署
vercel

# 生产环境部署
vercel --prod
```

## 部署状态

[![Deployed on Vercel](https://img.shields.io/badge/Vercel-Ready%20for%20Deploy-brightgreen)](https://vercel.com)

## 技术栈

- 后端：Python Flask
- 前端：HTML, CSS, JavaScript, Bootstrap 5
- 地图集成：百度地图API
- 测试：
  - 后端: unittest, flask_testing, coverage
  - 前端: Mocha, Chai
- 部署：Vercel 