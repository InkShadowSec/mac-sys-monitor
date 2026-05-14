# 🖥️ macOS System Monitor · Menu Bar Widget

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS-blue" alt="platform">
  <img src="https://img.shields.io/badge/python-3.9+-green" alt="python">
  <img src="https://img.shields.io/badge/license-MIT-orange" alt="license">
</p>

A lightweight macOS menu bar system monitor that displays real-time CPU, memory, and disk usage.

<img src="https://img.shields.io/badge/🟢-CPU_12%25-green" alt="demo">
<img src="https://img.shields.io/badge/MEM_61%25-blue" alt="demo">
<img src="https://img.shields.io/badge/DISK_18%25-purple" alt="demo">

## Features

- 📊 **Real-time monitoring** — CPU, memory, and disk usage, auto-refreshing every 3 seconds
- 🎨 **Status indicators** — 🟢 Normal / 🟡 Medium (>50%) / 🔴 High (>80%)
- 📈 **Top processes** — Shows the top 5 resource-consuming processes
- 🖱️ **Quick access** — One-click shortcut to open Activity Monitor
- 🪶 **Lightweight** — Minimal memory footprint, stays in the menu bar unobtrusively

## Preview

```
Menu bar: 🟢 CPU 12%  MEM 61%  DISK 18%
```

Click to expand:
```
CPU:  12.3%  (8 cores)
Memory: 61.3%  (7.8 GB / 16.0 GB  Free 6.2 GB)
Disk:  42.5%  (195.3 GB / 460.0 GB  Free 264.7 GB)

─ Top Processes ─
  Safari           15.2%   3.1%
  Chrome            8.5%   2.4%
  VS Code           6.1%   4.2%
  Slack             2.1%   1.5%

[Refresh] [Open Activity Monitor] [Quit]
```

## Quick Start

### Option 1: Run the Python script directly

```bash
# Install dependencies
pip install rumps psutil

# Run
python src/system_monitor.py
```

### Option 2: Build as a macOS App

```bash
# One-click build
chmod +x build.sh
./build.sh
```

This generates `系统监控.app` — double-click to run, no Python environment needed.

## Requirements

- macOS 11.0+
- Python 3.9+

## Project Structure

```
mac-sys-monitor/
├── src/
│   └── system_monitor.py   # Main application
├── build.sh                # Build script
├── requirements.txt        # Dependencies
├── LICENSE                 # MIT License
└── README_EN.md
```

## Technical Notes

- **rumps** — Native macOS menu bar framework built on PyObjC
- **psutil** — Cross-platform system information collection
- **shutil.disk_usage** — Accurately reads macOS APFS data volume disk usage (`psutil` incorrectly reads the read-only system volume)

## License

[MIT License](LICENSE)
