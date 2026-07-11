import streamlit as st

from pathlib import Path

from src import Directory


class MonsterModel:
    def __init__(self, name: str, width: int=720):
        self.name = name
        self.width = width
        self.path = Path.joinpath(Directory.scenario_monsters_dir(), f"{name}.svg")

    def render(self):
        with st.expander(self.name):
            st.image(self.path, width=self.width)