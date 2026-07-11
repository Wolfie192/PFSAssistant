import streamlit as st

from src.DataManager import DataManager


class VariableModel:
    def __init__(self, name: str):
        self.name = name
        self.manager = DataManager()

        all_data = self.manager.load_data()
        saved_state = all_data.get(self.name, None)

        if self.name not in st.session_state:
            st.session_state[self.name] = saved_state

        self.render()


    def _save(self):
        all_data = self.manager.load_data()
        all_data[self.name] = st.session_state[self.name]
        self.manager.save_data(all_data)


    def _load(self):
        all_data = self.manager.load_data()
        st.session_state[self.name] = all_data[self.name]


    def render(self):
        self._load()

        st.number_input(
            self.name,
            step=1,
            on_change=self._save,
            key=self.name
        )