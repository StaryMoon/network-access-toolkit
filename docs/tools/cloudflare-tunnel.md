# Cloudflare Tunnel

> 类型：`tunnel`
> 状态：**推荐**
> 难度：**中**

## 一句话

通过 cloudflared 建立出站隧道，不直接暴露本机公网端口。

## 适合谁

把本地 Web 服务安全暴露到公网、演示 demo、Webhook 回调测试

## 官方入口

- 官网：https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/
- GitHub：https://github.com/cloudflare/cloudflared
- 文档：https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/

## 开源情况

cloudflared 开源

## 成本说明

部分功能可免费使用，高级访问控制以 Cloudflare 当前计划为准。

## 优点

- 不需要公网 IP
- 适合 Web demo
- 能接 Cloudflare Access 做访问控制

## 缺点

- 绑定 Cloudflare 生态
- 非 Web/复杂 TCP 场景需要仔细看文档

## 典型场景

- 展示本地 Web 项目
- 测试 Webhook
- 给实验室服务加访问控制

## 安全提醒

不要把没有鉴权的服务直接暴露到公网。远程访问工具只解决连通性，不替你解决权限、审计和最小暴露面。

## Tags

`cloudflare`, `tunnel`, `web`, `zero-trust`
