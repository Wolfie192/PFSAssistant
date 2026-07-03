import streamlit as st
import json

from pathlib import Path

from ReadAloudModel import ReadAloudModel
from TextModel import TextModel
from ImageModel import ImageModel
from InfoBoxModel import InfoBoxModel


class ScenarioModel:
    def __init__(self, file_path: Path):
        self.data_path = file_path
        self.name = None
        self.season = None
        self.tier = []
        self.tags = []
        self.data = None

    def _get_scenario_data(self):
        if not self.data_path.exists():
            st.warning(f"No scenario data found at {self.data_path}")

        with open(self.data_path, "r", encoding="utf-8") as f:
            return json.load(f)


    def parse(self):
        data = self._get_scenario_data()
        metadata = data["metadata"]

        self.name = metadata["name"]
        self.season = metadata["season"]
        self.tier = [metadata["tier"]["min"], metadata["tier"]["max"]]
        self.tags = metadata["tags"]

        content = data["content"]

        for page in content.get("pages"):
            print(page)


if __name__ == "__main__":
    model = ScenarioModel(Path("E:/PFSAssistant/bin/scenario_data/season_7/scenario_21/scenario_data.json"))
    model.parse()