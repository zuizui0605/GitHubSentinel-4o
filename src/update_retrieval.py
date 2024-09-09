import requests

class UpdateRetrieval:
    def __init__(self, api_key):
        self.github_api_url = "https://api.github.com/repos/"
        self.api_key = api_key

    def fetch_updates(self, repos):
        updates = {}
        headers = {"Authorization": f"token {self.api_key}"}
        for repo in repos:
            url = f"${self.github_api_url}{repo}/events"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                updates[repo] = response.json()
            else:
                updates[repo] = []
        return updates
