from subscription_manager import SubscriptionManager
from update_retrieval import UpdateRetrieval
from notification_system import NotificationSystem
from report_generator import ReportGenerator
from config import Config
from exceptions import GitHubSentinelError

class GitHubSentinel:
    def __init__(self):
        self.config = Config()  # 加载配置
        self.sub_manager = SubscriptionManager()
        self.update_retrieval = UpdateRetrieval(self.config.get("GITHUB_API_KEY"))
        self.notification_system = NotificationSystem(
            method=self.config.get("NOTIFICATION_METHOD"),
            email=self.config.get("NOTIFICATION_EMAIL"),
            slack_webhook=self.config.get("NOTIFICATION_SLACK_WEBHOOK")
        )
        self.report_generator = ReportGenerator()

    def run(self):
        try:
            # 1. 获取用户的订阅仓库
            repos = self.sub_manager.get_subscribed_repos()

            # 2. 获取每个仓库的更新
            updates = self.update_retrieval.fetch_updates(repos)

            # 3. 生成更新报告
            report = self.report_generator.generate_report(updates)

            # 4. 发送通知
            self.notification_system.send_notification(report)
        
        except GitHubSentinelError as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    from scheduler import Scheduler
    config = Config()
    scheduler = Scheduler()
    scheduler.start(interval=config.get("SCHEDULE_INTERVAL", "daily"))
