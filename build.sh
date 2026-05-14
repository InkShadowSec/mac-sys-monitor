#!/bin/bash
# ========================================
# macOS 系统监控 - 构建脚本
# 生成独立 .app，不需要 Python 环境
# ========================================
set -e

echo "📦 安装依赖..."
python3 -m venv /tmp/sysmonitor_build
source /tmp/sysmonitor_build/bin/activate
pip install rumps psutil pyinstaller -q

echo "🔨 打包中（约 1-2 分钟）..."
pyinstaller --onefile --windowed --name "系统监控" --clean --noconfirm src/system_monitor.py

# 移动到项目根目录
mv dist/系统监控.app ./
rm -rf build dist src/system_monitor.spec /tmp/sysmonitor_build

echo ""
echo "✅ 完成！系统监控.app 已生成在项目根目录"
echo "   双击即可运行，菜单栏常驻显示 CPU/内存/磁盘"
