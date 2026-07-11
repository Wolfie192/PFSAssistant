import streamlit as st

from pathlib import Path

from src import Directory


class Monster:
    def __init__(self, name: str, init_mod: int, hp: int, img_name: str|None = None, img_ext: str = "svg", img_width: int=720):
        self.name = name
        self.init_mod = init_mod
        self.hp = hp
        self.damage = 0
        self.width = img_width
        img_name = img_name if img_name else name
        self.path = Path.joinpath(Directory.scenario_monsters_dir(), f"{img_name}.{img_ext}")

    def render(self):
        with st.expander(self.name):
            st.image(self.path, width=self.width)