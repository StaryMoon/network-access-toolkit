# VS Code Remote SSH

> 类型：`remote-dev`
> 状态：**科研刚需**
> 难度：**低到中**

## 一句话

VS Code 官方远程开发扩展，通过 SSH 在远端机器上开发。

## 适合谁

远程开发服务器、GPU 机器、实验室 Linux 环境

## 官方入口

- 官网：https://code.visualstudio.com/docs/remote/ssh
- GitHub：https://github.com/microsoft/vscode-remote-release
- 文档：https://code.visualstudio.com/docs/remote/ssh

## 开源情况

VS Code Remote 扩展发布方式以 Microsoft 官方为准

## 成本说明

VS Code 免费；远程机器成本另算。

## 优点

- 科研党高频刚需
- 编辑体验好
- 适合 GPU/服务器开发

## 缺点

- SSH 配置、跳板机、端口转发问题需要排障
- 远端扩展和 Python 环境偶尔会乱

## 典型场景

- A100/GPU 服务器开发
- 远程跑实验
- 论文代码调试

## 安全提醒

不要把没有鉴权的服务直接暴露到公网。远程访问工具只解决连通性，不替你解决权限、审计和最小暴露面。

## Tags

`vscode`, `ssh`, `remote-dev`, `gpu`
