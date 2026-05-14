#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
macOS 菜单栏系统监控小组件
显示 CPU、内存、磁盘使用率，点击查看详情。
运行：python3 mac系统监控.py
"""

import psutil
import rumps
import subprocess
import shutil


def format_gb(b):
    if b >= 1024:
        return f"{b:.1f} TB"
    return f"{b:.1f} GB"


class SystemMonitor(rumps.App):

    def __init__(self):
        super().__init__("Monitor", title="Monitor")

        # 固定菜单项
        self.cpu_item = rumps.MenuItem("CPU:  --")
        self.mem_item = rumps.MenuItem("内存: --")
        self.disk_item = rumps.MenuItem("磁盘: --")

        self.menu = [
            self.cpu_item,
            self.mem_item,
            self.disk_item,
            None,
        ]

        # Top 进程
        self.proc_title = rumps.MenuItem("─ 占用最高 ─")
        self.menu.add(self.proc_title)
        self.proc_items = [rumps.MenuItem("  ") for _ in range(5)]
        for item in self.proc_items:
            self.menu.add(item)

        self.menu.add(None)
        self.menu.add(rumps.MenuItem("刷新", callback=self._on_refresh))
        self.menu.add(rumps.MenuItem("打开活动监视器", callback=self._open_monitor))
        self.menu.add(None)
        self.menu.add(rumps.MenuItem("退出", callback=rumps.quit_application))

        self._update()

        # 每 3 秒刷新
        rumps.Timer(self._tick, 3).start()

    def _tick(self, _):
        self._update()

    def _update(self):
        # 采集数据
        cpu = psutil.cpu_percent(interval=0.3)
        mem = psutil.virtual_memory()
        disk = shutil.disk_usage("/")

        # 菜单详情
        self.cpu_item.title = f"CPU:  {cpu:.1f}%  ({psutil.cpu_count()} 核)"
        self.mem_item.title = (
            f"内存: {mem.percent:.1f}%  "
            f"({format_gb(mem.used/1024**3)} / {format_gb(mem.total/1024**3)}"
            f"  空闲 {format_gb(mem.available/1024**3)})"
        )
        disk_pct = disk.used * 100 / disk.total
        self.disk_item.title = (
            f"磁盘: {disk_pct:.1f}%  "
            f"({format_gb(disk.used/1024**3)} / {format_gb(disk.total/1024**3)}"
            f"  空闲 {format_gb(disk.free/1024**3)})"
        )

        # 状态指示
        if cpu > 80 or mem.percent > 80 or disk_pct > 85:
            indicator = "🔴"
        elif cpu > 50 or mem.percent > 50:
            indicator = "🟡"
        else:
            indicator = "🟢"

        self.title = f"{indicator} CPU {cpu:.0f}%  MEM {mem.percent:.0f}%  DISK {disk_pct:.0f}%"

        # Top 进程
        procs = []
        for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
            try:
                info = p.info
                if info["cpu_percent"] and info["cpu_percent"] > 0.1:
                    procs.append(info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        procs.sort(key=lambda x: x["cpu_percent"], reverse=True)

        for i in range(5):
            if i < len(procs):
                name = procs[i]["name"][:18]
                cpu_str = f"{procs[i]['cpu_percent']:.1f}%"
                mem_str = f"{procs[i]['memory_percent']:.1f}%"
                self.proc_items[i].title = f"  {name:<18} {cpu_str:>6}  {mem_str:>6}"
            else:
                self.proc_items[i].title = ""

    def _on_refresh(self, _):
        self._update()

    @staticmethod
    def _open_monitor(_):
        subprocess.run(["open", "-a", "活动监视器"])


if __name__ == "__main__":
    SystemMonitor().run()
