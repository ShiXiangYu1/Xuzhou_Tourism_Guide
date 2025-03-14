#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试文件自动转换脚本
自动修改所有测试文件，使其适应不同环境
"""

import os
import re
import glob
import shutil
import argparse


def backup_test_files(test_dir):
    """备份所有测试文件"""
    # 创建备份目录
    backup_dir = os.path.join(test_dir, 'backup')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # 备份所有测试文件
    for file_path in glob.glob(os.path.join(test_dir, 'test_*.py')):
        if 'test_base_alt.py' in file_path or 'test_base_selector.py' in file_path:
            continue
        
        backup_path = os.path.join(backup_dir, os.path.basename(file_path))
        shutil.copy2(file_path, backup_path)
        print(f"已备份: {file_path} -> {backup_path}")

    return backup_dir


def convert_test_file(file_path):
    """转换测试文件，添加自适应导入逻辑"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查文件是否已经包含自适应导入逻辑
    if 'flask_testing_available' in content:
        print(f"跳过已转换的文件: {file_path}")
        return
    
    # 正则表达式匹配导入 BaseTestCase 的行
    import_pattern = r'^from app\.tests\.test_base import BaseTestCase\s*$'
    
    # 替换导入语句为自适应导入逻辑
    adaptive_import = """import importlib.util

# 尝试导入标准测试基类，如果失败则使用替代测试基类
try:
    # 检查 flask_testing 是否可用
    flask_testing_available = importlib.util.find_spec("flask_testing") is not None
    
    if flask_testing_available:
        from app.tests.test_base import BaseTestCase
    else:
        # 使用替代测试基类
        from app.tests.test_base_alt import BaseTestCaseAlt as BaseTestCase
        print("注意: 使用替代测试基类 BaseTestCaseAlt")
except ImportError as e:
    # 导入失败时使用替代测试基类
    from app.tests.test_base_alt import BaseTestCaseAlt as BaseTestCase
    print(f"导入错误，使用替代测试基类: {e}")"""
    
    # 使用正则表达式替换
    modified_content = re.sub(import_pattern, adaptive_import, content, flags=re.MULTILINE)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"已转换: {file_path}")


def convert_all_test_files(test_dir):
    """转换所有测试文件"""
    for file_path in glob.glob(os.path.join(test_dir, 'test_*.py')):
        # 排除基类测试文件和选择器
        if 'test_base.py' in file_path or 'test_base_alt.py' in file_path or 'test_base_selector.py' in file_path:
            continue
        
        convert_test_file(file_path)


def restore_test_files(test_dir, backup_dir):
    """恢复测试文件原始版本"""
    for backup_path in glob.glob(os.path.join(backup_dir, 'test_*.py')):
        dest_path = os.path.join(test_dir, os.path.basename(backup_path))
        shutil.copy2(backup_path, dest_path)
        print(f"已恢复: {backup_path} -> {dest_path}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='自动转换测试文件以适应不同环境')
    parser.add_argument('--test-dir', default='app/tests', help='测试文件目录')
    parser.add_argument('--restore', action='store_true', help='恢复原始测试文件')
    args = parser.parse_args()
    
    test_dir = args.test_dir
    
    if args.restore:
        backup_dir = os.path.join(test_dir, 'backup')
        if os.path.exists(backup_dir):
            restore_test_files(test_dir, backup_dir)
            print("\n测试文件已恢复到原始版本")
        else:
            print("\n没有找到备份目录，无法恢复")
    else:
        print("\n开始转换测试文件...")
        backup_dir = backup_test_files(test_dir)
        convert_all_test_files(test_dir)
        print("\n测试文件转换完成")
        print(f"原始文件备份在 {backup_dir} 目录")
        print("如果需要恢复，请运行: python convert_test_files.py --restore")


if __name__ == "__main__":
    main() 