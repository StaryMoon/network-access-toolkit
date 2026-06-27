# WireGuard

> 类型：`vpn-protocol`
> 状态：**基础设施**
> 难度：**中**

## 一句话

现代、简洁、高性能 VPN 协议，很多组网工具底层都与 WireGuard 有关。

## 适合谁

想理解现代 VPN 基础、搭建轻量点对点隧道的人

## 官方入口

- 官网：https://www.wireguard.com/
- GitHub：https://git.zx2c4.com/wireguard-tools/
- 文档：https://www.wireguard.com/quickstart/

## 开源情况

开源

## 成本说明

软件免费；需要自备服务器或可互联设备。

## 优点

- 协议简洁
- 性能好
- 配置文件透明
- 适合学习网络隧道原理

## 缺点

- 需要自己处理密钥、路由、防火墙和 NAT
- 多设备管理不如 mesh 工具省心

## 典型场景

- 自建点对点 VPN
- 服务器安全访问
- 学习网络隧道和路由

## 安全提醒

不要把没有鉴权的服务直接暴露到公网。远程访问工具只解决连通性，不替你解决权限、审计和最小暴露面。

## Tags

`vpn`, `protocol`, `linux`, `networking`
