import streamlit as st
import html
import base64

from pathlib import Path


class ImageModel():
    """
    Model for displaying images within a scenario page.
    """
    def __init__(self, image_path: Path):
        self.image_path = image_path
        self.image_data = self._get_image_base64()


    def _get_image_base64(self):
        """
        Converts a local image/svg file to a base64 string.
        """
        if not self.image_path.exists():
            return None

        ext = self.image_path.suffix.lower()
        mime_type = "image/svg+xml" if ext == ".svg" else f"image/{ext.replace(".", "")}"

        with open(self.image_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f"data:{mime_type};base64,{data}"


    def render(self):
        if not self.image_path.exists():
            st.warning(f"No image found at {self.image_path}")
            return

        st.markdown(
            f"""
            <style>
            img {{
                display: block;
                max-width: 100%;
                height: auto;
            }}
            </style>
            <div>
                <img src="{self.image_data}">
            </div>
            """,
            unsafe_allow_html=True
        )