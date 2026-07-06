import streamlit as st


class SubsectionHeaderModel:
    def __init__(self, text: str):
        self.content = [text]

        self.render()


    def render(self):
        st.markdown(f"#### :gray[{self.content[0]}]")