from __future__ import annotations

import streamlit as st

from src.state import SessionStateModel


class PFSAssistantStreamlitApp:
    """Thin app wrapper around Streamlit plus a shared session-state adapter.

    This is intentionally small. It centralizes the Streamlit entry points and
    session-state access without trying to become a full controller layer.
    """

    def __init__(self, state_store=None):
        self.state = SessionStateModel(state_store if state_store is not None else st.session_state)

    def __getattr__(self, name):
        return getattr(st, name)

    def image(self, image_path, width=720, **kwargs):
        st.image(image_path, width=width, **kwargs)

    def text(self, content, indent="first_line"):
        if indent == "first_line":
            st.markdown(f"&emsp;{content}")
        else:
            st.markdown(content)

    def read_aloud(self, content):
        with st.container(border=True):
            for index, paragraph in enumerate(content):
                if index == 0:
                    st.markdown(f":green[{paragraph}]")
                else:
                    st.markdown(f"&emsp;:green[{paragraph}]")

    def section_header(self, content):
        st.markdown(f"## :gray[{content}]")

    def subsection_header(self, content):
        st.markdown(f"#### :gray[{content}]")
