import requests

class UpdateRetrieval:
    def __init__(self, api_key):
        self.github_api_url = "https://api.github.com/repos/"
        self.api_key = api_key

    def fetch_latest_release(self, repo):
        headers = {"Authorization": f"token {self.api_key}"}
        url = f"{self.github_api_url}{repo}/releases/latest"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch release data for {repo}: {response.status_code}")

    def fetch_updates_for_repos(self, repos):
        updates = {}
        for repo in repos:
            try:
                release_info = self.fetch_latest_release(repo)
                updates[repo] = release_info
            except Exception as e:
                print(f"Error fetching release for {repo}: {e}")
        return updates
