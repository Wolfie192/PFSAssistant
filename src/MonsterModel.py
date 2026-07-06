import streamlit as st

from pathlib import Path

from src.ImageModel import ImageModel


class MonsterModel:
    def __init__(self, name: str, path: Path):
        self.name = name
        self.path = path

    def render(self):
        with st.expander(self.name):
            ImageModel(self.path)