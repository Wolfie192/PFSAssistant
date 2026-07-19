import streamlit as st

from pathlib import Path

from src import Directory


def page(title: str, file_name: str):
    return st.Page(Path.joinpath(Directory.scenario_pages_dir(), f"{file_name}.py"), title=title)