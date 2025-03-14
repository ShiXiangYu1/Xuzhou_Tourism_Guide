#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
灵活的测试运行脚本
适应不同环境和依赖配置
"""

import os
import sys
import unittest
import importlib.util

# 添加项目根目录到 Python 模块搜索路径
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def check_dependencies():
    """检查测试依赖是否可用，返回可用的依赖列表"""
    available_deps = {
        "flask_testing": importlib.util.find_spec("flask_testing") is not None,
        "coverage": importlib.util.find_spec("coverage") is not None,
        "pytest": importlib.util.find_spec("pytest") is not None
    }
    
    print("\n环境依赖检查:")
    for dep, available in available_deps.items():
        status = "✓ 可用" if available else "✗ 不可用"
        print(f"  {dep}: {status}")
    print()
    
    return available_deps


def run_tests():
    """运行测试并生成报告"""
    deps = check_dependencies()
    
    # 创建测试套件
    test_suite = unittest.defaultTestLoader.discover('app/tests', pattern='test_*.py')
    
    # 使用 unittest 运行测试
    print("使用 unittest 运行测试...")
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    # 如果 coverage 可用，生成覆盖率报告
    if deps["coverage"]:
        try:
            import coverage
            print("\n生成覆盖率报告...")
            cov = coverage.Coverage(config_file="app/tests/.coveragerc")
            cov.start()
            
            # 再次运行测试以收集覆盖率数据
            test_loader = unittest.defaultTestLoader
            test_suite = test_loader.discover('app/tests', pattern='test_*.py')
            runner = unittest.TextTestRunner(verbosity=0)  # 使用较低的详细程度避免重复输出
            runner.run(test_suite)
            
            cov.stop()
            cov.save()
            
            print("\n覆盖率报告:")
            cov.report()
            
            # 生成HTML覆盖率报告
            cov.html_report(directory='coverage_html_report')
            print("\nHTML覆盖率报告已生成到 coverage_html_report 目录")
        except Exception as e:
            print(f"\n生成覆盖率报告时出错: {e}")
    
    # 如果 pytest 可用，也使用它运行测试
    if deps["pytest"]:
        try:
            print("\n使用 pytest 运行测试...")
            import pytest
            pytest.main(['-xvs', 'app/tests'])
        except Exception as e:
            print(f"\n使用 pytest 运行测试时出错: {e}")
    
    # 返回测试结果
    return len(result.errors) == 0 and len(result.failures) == 0


def provide_offline_instructions():
    """提供离线安装测试依赖的指南"""
    print("\n=== 离线安装测试依赖指南 ===")
    print("如果您在安装测试依赖时遇到网络问题，请尝试以下离线安装方法:")
    print("\n1. 在有网络连接的环境中下载依赖包:")
    print("   pip download -d ./deps flask-testing==0.8.1 coverage==7.3.2 pytest==7.4.0 pytest-cov==4.1.0")
    print("\n2. 将 deps 文件夹复制到您的目标环境")
    print("\n3. 在目标环境中安装依赖:")
    print("   pip install --no-index --find-links=./deps flask-testing coverage pytest pytest-cov")
    print("\n或者尝试以下替代安装命令:")
    print("   pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org flask-testing")
    print("   pip install -i https://mirrors.aliyun.com/pypi/simple/ flask-testing")
    print("\n如果仍然无法安装依赖，您可以使用 app/tests/test_base_alt.py 中的替代测试基类")
    print("详情请参考 app/tests/README.md 文件")


if __name__ == "__main__":
    # 运行测试
    success = run_tests()
    
    # 提供离线安装指南
    if not check_dependencies()["flask_testing"]:
        provide_offline_instructions()
    
    # 设置退出码
    sys.exit(0 if success else 1) 