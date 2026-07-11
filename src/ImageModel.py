import streamlit as st

from pathlib import Path

from src import Directory


class Image:
    def __init__(self, name: str, ext: str = "svg", width: int = 720):
        self.path = Path.joinpath(Directory.scenario_images_dir(), f"{name}.{ext}")
        self.width = width

        self.render()

    def render(self):
        st.image(self.path, width = self.width)