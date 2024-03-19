# SSH Trap Manager
文档语言：英语（English） | 简体中文（当前文档）
## 简介
SSH Trap Manager 是一个基于 [droberson/ssh-honeypot](https://github.com/droberson/ssh-honeypot) 项目开发的蜜罐管理工具。

**注意：目前处于开发阶段，绝大多数功能尚未完成。带有 * 符号的 Feature 为开发计划，目前尚未实现。**
## 特性
- *管理多台机器的蜜罐；
- *支持导出每日/指定时间段概况；
- 支持解析日志到其他格式
  - JSON；
  - *CSV；
  - *Excel；
  - *YAML；
  - *HTML（Markdown 渲染）；
- *支持接入钉钉机器人（待开发）；
- *支持一键部署，监听多台机器的蜜罐；
## 常见问题
Q: 我应该选择哪个版本？

A: 对于 `Windows` 用户，使用前缀为 `win-` 的版本，例如 `win-ssh-trap-manager`。

   对于 `Linux 用户`，使用前缀为 `linux-` 的版本，例如 `linux-ssh-trap-manager`。

   对于 `Mac` 及其它版本，你可以下载源代码自行编译。
   
Q: 如何使用？

A: 参考 SSH Trap Manager Wiki。需要注意的是，英文版本的 Wiki 更新稍慢，你可以先查阅中文版本的 Wiki。