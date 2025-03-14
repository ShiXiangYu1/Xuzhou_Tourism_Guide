# 徐州旅游攻略网站 - Vercel部署指南

本文档介绍如何将徐州旅游攻略网站部署到Vercel平台。

## 前提条件

1. 一个Vercel账号 - 您可以在[vercel.com](https://vercel.com)上免费注册
2. 本地Git仓库或者GitHub/GitLab/Bitbucket仓库
3. Node.js环境(用于安装Vercel CLI)

## 部署方法

### 方法一：通过Vercel网站部署（推荐）

1. **将代码推送到GitHub仓库**
   - 如果您还没有GitHub账号，请先在[github.com](https://github.com)注册
   - 创建一个新的仓库
   - 将项目代码推送到该仓库

2. **在Vercel中导入项目**
   - 登录Vercel账号
   - 点击"New Project"
   - 选择包含您项目的GitHub仓库
   - 点击"Import"

3. **配置部署设置**
   - Framework Preset: 选择"Other"
   - Build Command: 留空
   - Output Directory: 留空
   - Root Directory: 留空(使用项目根目录)

4. **配置环境变量**
   - 展开"Environment Variables"部分
   - 添加以下环境变量:
     - `SECRET_KEY`: 一个复杂的随机字符串作为密钥
     - `VERCEL_ENV`: `production`

5. **完成部署**
   - 点击"Deploy"按钮
   - 等待部署完成
   - 成功后，您将获得一个Vercel提供的URL，可以访问您的网站

### 方法二：通过Vercel CLI部署

1. **安装Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **初始化部署**
   - 在项目根目录下打开终端
   - 执行以下命令:
   ```bash
   vercel login  # 首次使用需要登录
   vercel        # 开始部署
   ```

3. **按照提示操作**
   - 确认项目设置
   - 设置环境变量
   - 确认部署

4. **生产环境部署**
   - 当您准备部署到生产环境时，使用:
   ```bash
   vercel --prod
   ```

## 更新已部署的项目

每当您推送新的代码到GitHub仓库时，Vercel会自动重新部署您的应用。您也可以通过以下方式手动触发部署:

1. **通过Vercel网站**
   - 登录Vercel控制台
   - 选择您的项目
   - 点击"Deployments"选项卡
   - 点击"Redeploy"按钮

2. **通过Vercel CLI**
   ```bash
   vercel --prod
   ```

## 自定义域名

您可以为您的Vercel项目设置自定义域名:

1. 登录Vercel控制台
2. 选择您的项目
3. 点击"Domains"选项卡
4. 点击"Add"按钮
5. 输入您的域名并按照提示操作

## 故障排除

如果您在部署过程中遇到问题:

1. **查看构建日志**
   - 在Vercel控制台中查看详细的构建和部署日志

2. **常见问题**
   - 确保您的`requirements.txt`中包含了所有必要的依赖
   - 确保`api/index.py`文件正确配置
   - 确保您的应用在非开发环境下也能正常工作

3. **其他资源**
   - [Vercel文档](https://vercel.com/docs)
   - [Vercel Python示例](https://github.com/vercel/examples/tree/main/python) 