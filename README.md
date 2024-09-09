# Release v0.1: Interactive CLI with Repository Management and Scheduler
## 主要功能：
- **交互式命令行工具**：用户现在可以在运行工具后进入交互模式，动态输入命令，而不需要每次使用都重新运行。
- **仓库管理**：
  - 添加、删除 GitHub 仓库订阅。
  - 查看所有已订阅的 GitHub 仓库列表。
- **手动和自动获取更新**：
  - 用户可以通过 fetch 命令手动获取所有订阅仓库的最新更新。
  - 支持通过 scheduler_start 命令启动后台定时任务，定期获取更新。
  - 支持通过 scheduler_stop 命令停止后台任务。
- **命令帮助**：启动工具时会自动打印使用指南，并支持 help 命令查看所有可用命令。
- **退出工具**：通过 exit 命令退出工具并停止所有后台任务。

## 示例命令：
- 添加仓库订阅：add <repo>
- 删除仓库订阅：remove <repo>
- 查看订阅列表：list
- 手动获取更新：fetch
- 启动 Scheduler：scheduler_start
- 停止 Scheduler：scheduler_stop
- 退出工具：exit
