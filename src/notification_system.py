class NotificationSystem:
    def __init__(self, method="email", email=None, slack_webhook=None):
        self.method = method
        self.email = email
        self.slack_webhook = slack_webhook

    def send_notification(self, report):
        if self.method == "email" and self.email:
            self.send_email(report)
        elif self.method == "slack" and self.slack_webhook:
            self.send_slack(report)
        else:
            print("No valid notification method configured.")

    def send_email(self, report):
        # 伪代码：通过 SMTP 发送邮件
        print(f"Sending report via email to {self.email}")
        print(report)

    def send_slack(self, report):
        # 伪代码：通过 Slack Webhook 发送消息
        print(f"Sending report to Slack webhook {self.slack_webhook}")
        print(report)
