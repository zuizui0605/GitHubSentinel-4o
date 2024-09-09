import threading
import time
import schedule
import cmd
from subscription_manager import SubscriptionManager
from update_retrieval import UpdateRetrieval
from report_generator import ReportGenerator
from config import Config

class GitHubSentinel(cmd.Cmd):
    prompt = 'github-sentinel> '  # 设置交互式命令提示符

    def __init__(self):
        super().__init__()
        self.config = Config()
        self.sub_manager = SubscriptionManager()
        self.update_retrieval = UpdateRetrieval(self.config.get("GITHUB_API_KEY"))
        self.report_generator = ReportGenerator()
        self.scheduler_running = False
        self.scheduler_thread = None

        # 打印工具使用指南
        self.print_welcome_message()

    def print_welcome_message(self):
        """打印工具的欢迎信息和基本用法"""
        welcome_message = """
欢迎使用 GitHubSentinel 交互式命令行工具！
您可以通过以下命令来管理 GitHub 仓库的订阅、手动获取更新和启动后台任务：

可用命令：
  add <repo>            添加仓库订阅 (格式：owner/repo)
  remove <repo>         删除仓库订阅
  list                  列出所有订阅的仓库
  fetch                 手动获取订阅仓库的更新
  scheduler_start       启动后台定时任务 Scheduler
  scheduler_stop        停止后台定时任务 Scheduler
  help                  查看命令的帮助信息
  exit                  退出工具
"""
        print(welcome_message)

    def fetch_updates(self):
        repos = self.sub_manager.get_subscribed_repos()
        if repos:
            updates = self.update_retrieval.fetch_updates_for_repos(repos)
            report = self.report_generator.generate_report(updates)
            print(report)
        else:
            print("没有订阅任何仓库。")

    def start_scheduler(self):
        if not self.scheduler_running:
            self.scheduler_running = True
            schedule.every().day.at("09:00").do(self.fetch_updates)
            print("Scheduler started...")

            def run_scheduler():
                while self.scheduler_running:
                    schedule.run_pending()
                    time.sleep(1)

            self.scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
            self.scheduler_thread.start()

    def stop_scheduler(self):
        if self.scheduler_running:
            self.scheduler_running = False
            print("Scheduler stopped...")

    # 命令：添加仓库订阅
    def do_add(self, arg):
        """添加仓库订阅: add <repo>"""
        repo_name = arg.strip()
        if repo_name:
            self.sub_manager.add_repo(repo_name)
        else:
            print("请输入仓库名称 (格式：owner/repo)")

    # 命令：删除仓库订阅
    def do_remove(self, arg):
        """删除仓库订阅: remove <repo>"""
        repo_name = arg.strip()
        if repo_name:
            self.sub_manager.remove_repo(repo_name)
        else:
            print("请输入仓库名称 (格式：owner/repo)")

    # 命令：列出订阅的仓库
    def do_list(self, arg):
        """列出所有订阅的仓库: list"""
        repos = self.sub_manager.get_subscribed_repos()
        if repos:
            print("订阅的仓库列表:")
            for repo in repos:
                print(f"- {repo}")
        else:
            print("没有订阅任何仓库。")

    # 命令：手动获取更新
    def do_fetch(self, arg):
        """手动获取订阅仓库的更新: fetch"""
        self.fetch_updates()

    # 命令：启动 Scheduler
    def do_scheduler_start(self, arg):
        """启动后台 Scheduler: scheduler_start"""
        self.start_scheduler()

    # 命令：停止 Scheduler
    def do_scheduler_stop(self, arg):
        """停止后台 Scheduler: scheduler_stop"""
        self.stop_scheduler()

    # 自定义 help 命令
    def do_help(self, arg):
        """显示工具的帮助信息"""
        self.print_welcome_message()

    # 命令：退出工具
    def do_exit(self, arg):
        """退出工具: exit"""
        self.stop_scheduler()
        print("退出工具...")
        return True  # 返回 True 退出交互式命令行

    # 处理未知命令
    def default(self, line):
        print(f"未知命令: {line}")
        print("输入 'help' 查看可用命令。")

if __name__ == "__main__":
    sentinel = GitHubSentinel()
    sentinel.cmdloop()  # 进入交互式命令行
