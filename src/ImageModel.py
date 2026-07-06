import streamlit as st

from pathlib import Path


class ImageModel:
    def __init__(self, image_path: Path, width: int = 720):
        self.file_path = image_path
        self.width = width

        self.render()

    def render(self):
        st.image(self.file_path, width = self.width)