import schedule
import time
from sentinel import GitHubSentinel

class Scheduler:
    def __init__(self):
        self.sentinel = GitHubSentinel()

    def job(self):
        print("Running scheduled GitHub Sentinel job...")
        self.sentinel.run()

    def start(self, interval="daily"):
        # 根据配置文件中的设置，启动不同频率的定时任务
        if interval == "daily":
            schedule.every().day.at("09:00").do(self.job)  # 每天9点运行
        elif interval == "weekly":
            schedule.every().monday.at("09:00").do(self.job)  # 每周一9点运行

        while True:
            schedule.run_pending()
            time.sleep(1)
