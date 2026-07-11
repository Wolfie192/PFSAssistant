import json

from pathlib import Path

from src import Directory


class DataManager:
    def __init__(self, file_path: Path = Directory.scenario_state_path()):
        self.file_path = file_path


    def load_data(self):
        if self.file_path.exists():
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}


    def save_data(self, data_dict):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data_dict, f, indent=4)


    def get_model_data(self, model_id):
        all_data = self.load_data()
        return all_data.get(str(model_id), {})