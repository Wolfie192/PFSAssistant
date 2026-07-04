import streamlit as st

from pathlib import Path


class ImageModel():
    """
    Model for displaying images within a scenario page.
    """
    def __init__(self, image_path: Path, width: int|None = None):
        self.image_path = image_path
        self.width = width if width else 720


    def render(self):
        if not self.image_path.exists():
            st.warning(f"No image found at {self.image_path}")
            return

        st.image(self.image_path, width=self.width)