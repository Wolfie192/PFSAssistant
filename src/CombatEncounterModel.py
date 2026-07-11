import streamlit as st

from src.DataManager import DataManager
from src.MonsterModel import Monster
from src.ImageModel import Image


class CombatEncounterModel:
    def __init__(self, name: str, enemies: list[Monster], model_id: str):
        self.name = name
        self.id = model_id
        self.enemies = enemies
        self.manager = DataManager()

        self.render()


    def render(self):
        with st.expander(self.name):
            for enemy in self.enemies:
                with st.expander(enemy.name):
                    with st.container(border=True):
                        Image(enemy.path, width=enemy.width)