import streamlit as st

from src.DataManager import DataManager


class Variable:
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


    def render(self):
        st.session_state[self.name] = st.number_input(
            self.name,
            step=1,
            value=st.session_state[self.name]
        )