import streamlit as st

from pathlib import Path

from src import Directory


def page(title: str):
    page_name = title.lower()

    replacements = {
        " ": "_",
        "?": "",
        ".": "",
        "(": "",
        ")": "",
        ":": ""
    }

    for old, new in replacements.items():
        page_name = page_name.replace(old, new)

    page_name += ".py"

    return st.Page(Path.joinpath(Directory.scenario_pages_dir(), page_name), title=title)