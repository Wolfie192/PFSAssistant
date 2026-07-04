import streamlit as st


class InfoBoxModel:
    """
    Model for displaying markdown formatted text and
    images within a formatted info box.
    """
    def __init__(self, content: list):
        self.content = content


    def render(self):
        if not self.content:
            st.info("Empty read aloud module.")
            return

        with st.container(border=True):
            for content in self.content:
                content.render()