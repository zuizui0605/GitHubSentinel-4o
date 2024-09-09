import json

class SubscriptionManager:
    def __init__(self, subscription_file="subscriptions.json"):
        self.subscription_file = subscription_file
        self.subscriptions = self.load_subscriptions()

    def load_subscriptions(self):
        try:
            with open(self.subscription_file, 'r') as file:
                data = json.load(file)
                return data.get("repositories", [])
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            raise Exception(f"Error decoding {self.subscription_file}: {str(e)}. Please check its format.")

    def save_subscriptions(self):
        try:
            with open(self.subscription_file, 'w') as file:
                json.dump({"repositories": self.subscriptions}, file, indent=4)
        except Exception as e:
            print(f"Failed to save subscriptions: {e}")

    def add_repo(self, repo_name):
        if repo_name not in self.subscriptions:
            self.subscriptions.append(repo_name)
            self.save_subscriptions()
            print(f"已添加订阅仓库: {repo_name}")
        else:
            print(f"仓库 {repo_name} 已经在订阅列表中。")

    def remove_repo(self, repo_name):
        if repo_name in self.subscriptions:
            self.subscriptions.remove(repo_name)
            self.save_subscriptions()
            print(f"已取消订阅仓库: {repo_name}")
        else:
            print(f"仓库 {repo_name} 不在订阅列表中。")

    def get_subscribed_repos(self):
        return self.subscriptions
