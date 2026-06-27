# Headscale

> 类型：`self-hosted-control-plane`
> 状态：**进阶**
> 难度：**中**

## 一句话

开源的 Tailscale 控制服务器实现，常用于自建私有 mesh 网络控制面。

## 适合谁

想要自建 Tailscale 控制面、减少对商业控制面的依赖

## 官方入口

- 官网：https://headscale.net/
- GitHub：https://github.com/juanfont/headscale
- 文档：https://headscale.net/stable/

## 开源情况

开源

## 成本说明

需要自备 VPS 或服务器，成本取决于云服务器。

## 优点

- 控制面自建
- 适合长期维护私有网络
- 和 Tailscale 客户端生态兼容度高

## 缺点

- 部署和维护成本高于 Tailscale 官方
- 需要理解域名、TLS、反向代理等概念

## 典型场景

- 实验室自建组网
- 个人长期网络基础设施
- 不想把控制面交给第三方

## 安全提醒

不要把没有鉴权的服务直接暴露到公网。远程访问工具只解决连通性，不替你解决权限、审计和最小暴露面。

## Tags

`tailscale`, `self-hosted`, `mesh-vpn`, `wireguard`
