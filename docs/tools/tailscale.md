# Tailscale

> 类型：`mesh-vpn`
> 状态：**首选**
> 难度：**低**

## 一句话

基于 WireGuard 的零配置 mesh VPN，适合大多数不想维护复杂网络的人。

## 适合谁

多设备互联、远程 SSH、访问家里 NAS/实验室机器、临时组队协作

## 官方入口

- 官网：https://tailscale.com/
- GitHub：https://github.com/tailscale/tailscale
- 文档：https://tailscale.com/kb

## 开源情况

客户端开源，服务端控制面由官方提供；可搭配 Headscale 自建控制面。

## 成本说明

个人和小团队通常可从免费计划开始，具体限制以官方页面为准。

## 优点

- 上手很快
- 跨平台
- 适合 SSH 和远程桌面
- NAT 穿透体验好

## 缺点

- 依赖官方控制面
- 高级团队功能可能需要付费
- 网络受限环境下仍需排障

## 典型场景

- 远程连实验室服务器
- 家里 NAS 外网访问
- 多台 Mac/Windows/Linux 互联

## 安全提醒

不要把没有鉴权的服务直接暴露到公网。远程访问工具只解决连通性，不替你解决权限、审计和最小暴露面。

## Tags

`mesh-vpn`, `wireguard`, `ssh`, `remote-access`
