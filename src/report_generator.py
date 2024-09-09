class ReportGenerator:
    def __init__(self):
        pass

    def generate_report(self, updates):
        report = "GitHub Sentinel Report\n"
        for repo, events in updates.items():
            report += f"\nRepository: {repo}\n"
            for event in events:
                report += f" - {event['type']} by {event['actor']['login']} at {event['created_at']}\n"
        return report
