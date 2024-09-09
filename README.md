# GitHubSentinel-4o

**GitHubSentinel-4o** 是一款开源的 AI 驱动代理，旨在帮助开发者和项目管理人员高效追踪他们订阅的 GitHub 仓库中的最新动态。该代理通过自动化地获取仓库变更和发送通知，减少了手动检查更新的工作量，从而提高了团队协作的效率。

## 主要功能：
- **自动更新获取**：自动从订阅的 GitHub 仓库获取最新变更（包括 Issues、Pull Requests、Commits 等）。
- **订阅管理**：简单易用的订阅管理系统，支持仓库的添加和移除。
- **定时任务调度**：可根据用户设置的计划（每日或每周）定期运行，确保及时获取更新。
- **通知系统**：根据配置，通过电子邮件或 Slack 发送更新通知。
- **自定义报告**：将仓库活动生成简洁明了的报告，方便用户快速查看。
- **灵活配置**：使用 JSON 配置文件存储设置，如 GitHub API 令牌、通知偏好和任务调度时间间隔。

## Getting Started & Configuration

按照以下步骤来快速启动并配置 **GitHubSentinel-4o**：

### 1. 克隆项目仓库

首先将项目仓库克隆到本地：

```bash
git clone https://github.com/yourusername/GitHubSentinel-4o.git
cd GitHubSentinel-4o
```
### 2. 安装依赖

确保你已经安装了 Python 3.x，然后使用 `pip` 安装所需的依赖项：

```bash
pip install -r requirements.txt
```
### 3. 配置项目
在 GitHubSentinel-4o 目录下，你会找到一个默认的配置文件 config.json。在继续之前，请编辑该文件，并将其中的 GitHub API 令牌和通知选项替换为你自己的设置。
```
{
    "GITHUB_API_KEY": "your_github_api_token",
    "NOTIFICATION_EMAIL": "your_email@example.com",
    "NOTIFICATION_SLACK_WEBHOOK": "your_slack_webhook_url",
    "SCHEDULE_INTERVAL": "daily", 
    "NOTIFICATION_METHOD": "email"
}
```
- **GITHUB_API_KEY:** 你的 GitHub 个人访问令牌（请前往 GitHub 生成令牌）。
- **NOTIFICATION_EMAIL:** 如果你选择通过电子邮件发送通知，请在此填入你的邮箱地址。
- **NOTIFICATION_SLACK_WEBHOOK:** 如果你选择通过 Slack 发送通知，请在此填入你的 Slack Webhook URL。
- **SCHEDULE_INTERVAL:** 可选 "daily"（每日）或 "weekly"（每周），定义定时任务的执行频率。
- **NOTIFICATION_METHOD:** 选择 "email" 或 "slack" 作为通知方式。

### 4. 运行项目
配置完成后，你可以通过以下命令启动 GitHubSentinel-4o：
```
python src/scheduler.py

```

