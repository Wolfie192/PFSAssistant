import streamlit as st

from pathlib import Path

from src import Directory


class ImageModel:
    def __init__(self, image_name: str, image_type: str = "svg", width: int = 720):
        self.file_path = Path.joinpath(Directory.scenario_images_dir(), f"{image_name}.{image_type}")
        self.width = width

        self.render()

    def render(self):
        st.image(self.file_path, width = self.width)