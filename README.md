# AI 驱动开发工作流

> 使用 Cursor + Linear + GitHub 实现自动化项目管理

## 项目简介

本项目演示如何通过 AI 驱动的工作流，实现：

- 📋 **任务自动同步** - 说"开始做"/"完成了"自动更新 Linear 状态
- 🔀 **代码规范提交** - AI 自动生成 Conventional Commits 格式
- 📊 **进度实时追踪** - 随时查看项目完成百分比

## 快速开始

1. 配置 Linear MCP
2. 复制 `.cursorrules` 到项目根目录
3. 对 AI 说"创建项目 XXX"

## 文档

- [01-AI驱动开发工作流详解](docs/01-AI驱动开发工作流详解.md) - 原理讲解
- [02-新项目使用指南](docs/02-新项目使用指南.md) - 实操步骤

## 核心文件

```
.cursorrules          # AI 规则配置（必须）
docs/                 # 教学文档
templates/            # 通用模板
```

## 常用指令

| 说 | 做 |
|----|-----|
| "创建项目 XXX" | 创建 Linear Project + Issues |
| "开始做 AUTH-1" | 状态 → In Progress |
| "完成了" | 状态 → Done |
| "提交代码" | git add + commit + push |
| "项目进度" | 显示完成百分比 |

## 许可证

MIT
