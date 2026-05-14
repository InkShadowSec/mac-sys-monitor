# 🖥️ macOS 系统监控 · 菜单栏小组件

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS-blue" alt="platform">
  <img src="https://img.shields.io/badge/python-3.9+-green" alt="python">
  <img src="https://img.shields.io/badge/license-MIT-orange" alt="license">
</p>

一个轻量级的 macOS 菜单栏系统监控工具，实时显示 CPU、内存和磁盘使用率。

<img src="https://img.shields.io/badge/🟢-CPU_12%25-green" alt="demo">
<img src="https://img.shields.io/badge/MEM_61%25-blue" alt="demo">
<img src="https://img.shields.io/badge/DISK_18%25-purple" alt="demo">

## 功能特性

- 📊 **实时监控** — CPU、内存、磁盘使用率，每 3 秒自动刷新
- 🎨 **状态指示** — 🟢 正常 / 🟡 中等(>50%) / 🔴 高负载(>80%)
- 📈 **进程排行** — 显示占用最高的 5 个进程
- 🖱️ **一键跳转** — 快速打开活动监视器
- 🪶 **轻量常驻** — 内存占用极小，菜单栏常驻不干扰

## 预览

```
菜单栏: 🟢 CPU 12%  MEM 61%  DISK 18%
```

点击展开：
```
CPU:  12.3%  (8 核)
内存: 61.3%  (7.8 GB / 16.0 GB  空闲 6.2 GB)
磁盘: 42.5%  (195.3 GB / 460.0 GB  空闲 264.7 GB)

─ 占用最高 ─
  Safari            15.2%   3.1%
  钉钉               8.5%   2.4%
  Chrome             6.1%   4.2%
  Code               2.1%   1.5%

[刷新] [打开活动监视器] [退出]
```

## 快速开始

### 方式一：直接运行 Python 脚本

```bash
# 安装依赖
pip install rumps psutil

# 运行
python src/system_monitor.py
```

### 方式二：打包为 macOS App

```bash
# 一键打包
chmod +x build.sh
./build.sh
```

打包后会生成 `系统监控.app`，双击即可运行，不需要 Python 环境。

## 系统要求

- macOS 11.0+
- Python 3.9+

## 项目结构

```
mac-sys-monitor/
├── src/
│   └── system_monitor.py   # 主程序
├── build.sh                # 打包脚本
├── requirements.txt        # 依赖
├── LICENSE                 # MIT 协议
└── README.md
```

## 技术细节

- **rumps** — macOS 原生菜单栏框架，基于 PyObjC
- **psutil** — 跨平台系统信息采集
- **shutil.disk_usage** — 准确读取 macOS APFS 数据卷的磁盘用量（`psutil` 会误读只读系统卷）

## 许可证

[MIT License](LICENSE)
