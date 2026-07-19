import streamlit as st

from pathlib import Path

from src import Directory


def image(img_name: str, ext: str = "svg", width=720):
    img_path = Path.joinpath(Directory.scenario_images_dir(), f"{img_name}.{ext}")

    st.image(img_path, width=width)