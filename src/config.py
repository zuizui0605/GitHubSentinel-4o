import json

class Config:
    def __init__(self, config_file="config.json"):
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        try:
            with open(config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception(f"Config file {config_file} not found.")
        except json.JSONDecodeError:
            raise Exception(f"Error decoding {config_file}. Please check its format.")

    def get(self, key, default=None):
        return self.config.get(key, default)
