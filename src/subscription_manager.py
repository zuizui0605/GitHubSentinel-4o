class SubscriptionManager:
    def __init__(self):
        # 假设从配置文件或数据库中获取订阅的仓库
        self.subscriptions = []

    def add_repo(self, repo_name):
        self.subscriptions.append(repo_name)

    def remove_repo(self, repo_name):
        self.subscriptions.remove(repo_name)

    def get_subscribed_repos(self):
        return self.subscriptions
