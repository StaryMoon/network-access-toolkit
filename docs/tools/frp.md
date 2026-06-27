# frp

> 类型：`reverse-proxy`
> 状态：**自建常用**
> 难度：**中**

## 一句话

高性能反向代理应用，常用于内网穿透、自建服务访问和 TCP/UDP 转发。

## 适合谁

有 VPS，想把内网服务映射到公网的人

## 官方入口

- 官网：https://github.com/fatedier/frp
- GitHub：https://github.com/fatedier/frp
- 文档：https://gofrp.org/

## 开源情况

开源

## 成本说明

软件免费；需要自备公网服务器。

## 优点

- 灵活
- 支持多协议
- 中文资料多
- 适合有服务器的人

## 缺点

- 需要自己维护服务端
- 安全配置必须认真做
- 公网暴露服务有风险

## 典型场景

- 内网 SSH
- 内网 Web 服务
- 开发测试和临时演示

## 安全提醒

不要把没有鉴权的服务直接暴露到公网。远程访问工具只解决连通性，不替你解决权限、审计和最小暴露面。

## Tags

`reverse-proxy`, `nat-traversal`, `self-hosted`
