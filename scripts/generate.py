#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "tools.json"
README = ROOT / "README.md"
DOCS = ROOT / "docs" / "tools"


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    tools = sorted(payload["tools"], key=lambda item: item["priority"])
    DOCS.mkdir(parents=True, exist_ok=True)
    README.write_text(render_readme(payload["meta"], tools), encoding="utf-8")
    for tool in tools:
        (DOCS / f"{tool['slug']}.md").write_text(render_tool(tool), encoding="utf-8")
    print(f"Generated README and {len(tools)} tool pages.")


def render_readme(meta: Dict[str, Any], tools: List[Dict[str, Any]]) -> str:
    lines = [
        '<h1 align="center">学生科研党网络连通性工具箱</h1>',
        "",
        '<p align="center">',
        "  <strong>远程服务器 · 自建组网 · 内网穿透 · SSH 排障 · 文件同步 · 合法网络工具</strong>",
        "</p>",
        "",
        "> 只收官方工具、自建方案和合法远程访问方案；不收机场购买链接、不收返利、不搬运测速图。",
        "",
        '<p align="center">',
        '  <img src="assets/network-access-map.svg" alt="学生科研党网络连通性工具箱结构图" width="920">',
        "</p>",
        "",
        f"最后人工核验：**{meta['last_verified']}**",
        "",
        "如果这个项目帮你少折腾一次 SSH、校园网、远程 GPU 或内网穿透，欢迎 star。后续会继续补充真实排障模板和科研场景配置。",
        "",
        "## 快速结论",
        "",
        "- **最省心多设备组网**：Tailscale。",
        "- **想自建控制面**：Headscale。",
        "- **虚拟局域网/多人设备互联**：ZeroTier。",
        "- **理解底层和自建点对点 VPN**：WireGuard。",
        "- **临时展示本地 Web demo**：Cloudflare Tunnel 或 ngrok。",
        "- **有 VPS 做内网穿透**：frp。",
        "- **远程 GPU/实验室机器开发**：VS Code Remote SSH + SSH config。",
        "- **弱网终端**：Mosh。",
        "- **同步数据集/实验结果**：rclone。",
        "",
        "## 场景速查",
        "",
        "| 场景 | 首选 | 备选 | 注意点 |",
        "| --- | --- | --- | --- |",
        "| 远程连实验室服务器 | VS Code Remote SSH | Mosh / Tailscale | 先保证 SSH key 和跳板机配置干净 |",
        "| 多台设备互联 | Tailscale | ZeroTier / Headscale | 免费计划和设备数限制看官方 |",
        "| 本地 Web demo 给别人看 | Cloudflare Tunnel | ngrok / frp | 不要暴露敏感后台 |",
        "| 家里 NAS 外网访问 | Tailscale | ZeroTier / frp | 注意账号安全和 ACL |",
        "| 有 VPS，想自建内网穿透 | frp | WireGuard | 公网服务必须加鉴权 |",
        "| 弱网长时间终端 | Mosh | tmux + SSH | Mosh 需要 UDP |",
        "| 大文件同步 | rclone | rsync / scp | 先 dry-run，避免同步方向反了 |",
        "",
        "## 工具总表",
        "",
        "| 优先级 | 工具 | 类型 | 状态 | 适合谁 | GitHub | 官方文档 |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for tool in tools:
        lines.append(
            "| {priority} | [{name}](docs/tools/{slug}.md) | `{category}` | {status} | {best_for} | [Repo]({github_url}) | [Docs]({docs_url}) |".format(
                priority=tool["priority"],
                name=tool["name"],
                slug=tool["slug"],
                category=tool["category"],
                status=tool["status"],
                best_for=escape_cell(tool["best_for"]),
                github_url=tool["github_url"],
                docs_url=tool["docs_url"],
            )
        )
    lines.extend(
        [
            "",
            "## 推荐组合",
            "",
            "### 研究生远程服务器开发",
            "",
            "```text",
            "VS Code Remote SSH + ~/.ssh/config + tmux + rclone",
            "```",
            "",
            "适合 GPU 服务器、实验室工作站、远程跑论文代码。",
            "",
            "### 家庭/宿舍/实验室多设备互联",
            "",
            "```text",
            "Tailscale 或 ZeroTier",
            "```",
            "",
            "适合访问 NAS、台式机、远程开发机，不想折腾公网 IP。",
            "",
            "### 自建党方案",
            "",
            "```text",
            "Headscale + WireGuard + frp",
            "```",
            "",
            "适合有 VPS、愿意维护证书、域名、反向代理和安全策略的人。",
            "",
            "## 网络安全底线",
            "",
            "- 不要把数据库、Jupyter、Docker API、开发后台裸露到公网。",
            "- 内网穿透服务必须有鉴权，最好再加 IP allowlist 或 Zero Trust。",
            "- SSH 禁用密码登录，使用 key，必要时加 2FA 或堡垒机。",
            "- 云服务器安全组只开必要端口。",
            "- 任何远程访问工具都不是免死金牌，配置错了就是公网裸奔。",
            "",
            "## 排障 checklist",
            "",
            "- `ping` 不通不代表 TCP 不通，先测具体端口。",
            "- SSH 失败先看 `ssh -vvv`。",
            "- 校园网/公司网可能封 UDP，Mosh、WireGuard、部分 NAT 穿透会受影响。",
            "- DNS 问题和路由问题分开查。",
            "- 先在同一局域网测通，再上公网/隧道。",
            "- 所有自动同步工具先 dry-run。",
            "",
            "## 数据维护",
            "",
            "结构化数据在 [`data/tools.json`](data/tools.json)。",
            "",
            "重新生成：",
            "",
            "```bash",
            "python3 scripts/generate.py",
            "```",
            "",
            "## 贡献原则",
            "",
            "欢迎补充：",
            "",
            "- 官方工具和开源项目",
            "- 学生/科研远程访问真实场景",
            "- SSH、隧道、组网、文件同步排障模板",
            "- 安全配置建议",
            "",
            "请不要提交：",
            "",
            "- 机场购买链接",
            "- 返利链接",
            "- 搬运测速图",
            "- 鼓励绕过学校/公司网络管理的教程",
            "- 未授权转载的测评内容",
            "",
            "## Disclaimer",
            "",
            "本项目只做合法网络连通性、远程访问和自建工具的信息整理。请遵守所在地法律法规、学校/机构网络管理规定和各项目 license/terms。",
            "",
            "## License",
            "",
            "MIT.",
            "",
        ]
    )
    return "\n".join(lines)


def render_tool(tool: Dict[str, Any]) -> str:
    pros = "\n".join(f"- {item}" for item in tool["pros"])
    cons = "\n".join(f"- {item}" for item in tool["cons"])
    use_cases = "\n".join(f"- {item}" for item in tool["use_cases"])
    tags = ", ".join(f"`{tag}`" for tag in tool["tags"])
    return f"""# {tool['name']}

> 类型：`{tool['category']}`
> 状态：**{tool['status']}**
> 难度：**{tool['difficulty']}**

## 一句话

{tool['summary']}

## 适合谁

{tool['best_for']}

## 官方入口

- 官网：{tool['official_url']}
- GitHub：{tool['github_url']}
- 文档：{tool['docs_url']}

## 开源情况

{tool['open_source']}

## 成本说明

{tool['cost_note']}

## 优点

{pros}

## 缺点

{cons}

## 典型场景

{use_cases}

## 安全提醒

不要把没有鉴权的服务直接暴露到公网。远程访问工具只解决连通性，不替你解决权限、审计和最小暴露面。

## Tags

{tags}
"""


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|")


if __name__ == "__main__":
    main()
