import streamlit as st


class SectionHeaderModel:
    def __init__(self, text: str):
        self.content = [text]

        self.render()


    def render(self):
        st.markdown(f"### :blue[{self.content[0]}]")