class ReportGenerator:
    def __init__(self):
        pass

    def generate_report(self, updates):
        report = "GitHub 仓库最新版本报告\n"
        for repo, release_info in updates.items():
            if release_info:
                report += f"\n仓库: {repo}\n"
                report += f"最新版本: {release_info['tag_name']}\n"
                report += f"发布者: {release_info['author']['login']}\n"
                report += f"发布时间: {release_info['published_at']}\n"
                report += f"更新日志: {release_info['body']}\n"
            else:
                report += f"\n仓库: {repo}\n未找到最新版本信息。\n"
        return report
